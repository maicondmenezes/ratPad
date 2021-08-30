from reports.models import RatPadrao
import json, csv
from datetime import datetime
from os import system, name
from inspect import getmembers, isclass

DATABASE = 'reports/tests/pDatabase.json'

def clear():      
    if name == 'nt':
        _ = system('cls')  
    else:
        _ = system('clear')

def filterTypeModule(module_name, filter_type):
    if(module_name.find(filter_type)!=-1):
        return True
    return False

def getTypeListFrom(module, type_name):
    type_list = []
    class_list = getmembers(module, isclass)
    for class_ in class_list:
        class_name = class_[0]
        if(filterTypeModule(class_name, type_name)):
            type_list.append(class_)
    
    return type_list

def getSerializerListFrom(modules_list):
    serializers_list = []
    for module in modules_list:
        module_name = module[0]
        if filterTypeModule(module_name, 'Serializer'):
            serializers_list.append(module)
    
    return serializers_list

def getDatabaseTypesTableFrom(modules):
    database_types = []
    type_list = getTypeListFrom(modules, 'Tipo')
    type_list += getTypeListFrom(modules, 'Local')    
    serializer_list = getSerializerListFrom(type_list)
    
    for itens in serializer_list:        
        object_type = itens[1]
        data_object = loadDataObjectFromSerializer(object_type)
        database_types.append(data_object)
    
    return database_types
    
def extractFirstObjectFromJson(json_filename):
    with open(json_filename, 'r') as json_file:
        object_list = json.load(json_file)
        object = object_list[0]
        if('fields' in object.keys()):
            return object['fields']
        return object

def createObject(object_type, data={}, many=False):    
    this_object = object_type(data=data, many=many)
    if(this_object.is_valid()):
        created_object = this_object.save()
        return created_object

    return this_object.errors

def loadDataObjectFromSerializer(serializer):    
    data_object = {
        "name": "",
        "type": serializer,
        "content": None,
        "result": None,
    }
    object_name = serializer.__name__.lower()
    data_object['name'] = object_name.replace('serializer', '')                         
    data_object['content'] = extractFirstObjectFromJson('reports/tests/data/'+data_object['name']+'.json')
    data_object['result'] = createObject(object_type=data_object['type'], data=data_object['content'], many=False)              
    
    return data_object

def loadDatabaseFromSerializerList(log_filename, serializers=[]): 
    database_itens = []   
    with open(log_filename, 'w') as logFile:
        logFile.write(f'Log atualizado: {datetime.now()}\n')      
       
        for serializer in serializers:
            data_object = loadDataObjectFromSerializer(serializer)
            logFile.write(
                f"\nCarregando: { data_object['name'] }"
                f"\nTipo:  {data_object['type']}"
                f"\nConteúdo:  {data_object['content']}"
                f"\nResposta: {data_object['result']}\n"                
            ) 
            database_itens.append(data_object)
    
    return database_itens

def getFullDatabaseFrom(serializers, log_filename):    
    database_itens = loadDatabaseFromSerializerList(log_filename, serializers)

    return database_itens
    
def extractObjectToJSON(object_list, object_filename):
    with open(object_filename, 'w') as object_file:
        object_file.write(json.dumps(object_list, indent=4))

def exportAnalistServicesCSV(user_id, filename):
    i = 0
    rats = RatPadrao.objects.filter(tecnico=user_id)
    with open(filename, mode='w') as f:
        csv_writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for rat in rats:
            csv_writer.writerow([
                rat.tecnico.first_name,
                rat.chamados,
                rat.data.strftime('%d'),
                rat.designacao.designacao,
                rat.designacao.nome
            ])
            i+=1
            clear()
            print(
                'Exportando Atendimentos: '+ 
                str(i) + ' | ' +
                str(len(rats))
            )  
    f.close()