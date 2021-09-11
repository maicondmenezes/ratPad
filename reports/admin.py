from django.contrib import admin
from django_object_actions import DjangoObjectActions
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

'''
Este módulo define os formulários de gestão das entidades do sistema no módulo administrativo do django
'''
  
class BaixaInLine(admin.TabularInline):
    '''
    Formulário em linha para cadastrar um Status de Baixa.
    Este formulário é referenciado no formulário de PArecer Técnico de Baixa
    '''
    model = StatusDeBaixa
    extra = 1
    raw_id_fields = ('computador',)

    def save_model(self, request, obj, change):
        '''Registra o usuário que criou o relatório no momento de salvá-lo
        Args:
            request: requisição http
            obj: um objeto do tipo RatPadrao
            change: status de alteração no obj
        Returns:
            HttpResponseRedirect: reverse('reports:report_padrao', args=(obj.id,))
        '''
        if not change:            
            obj.ativo = False
            obj.funcinando = False
        obj.save()    

class ComputadorInLine(admin.TabularInline):
    '''
    Formulário em linha para cadastrar um Computador.
    Este formulário é referenciado no formulário de Status De Baixa
    '''
    model = Computador
    extra = 1
    raw_id_fields = ('escola',)

class LinkDeInternetInLine(admin.TabularInline):
    '''
    Formulário em linha para cadastrar um Link de Internet.
    Este formulário é referenciado no formulário de Escola.    
    '''
    model = LinkDeInternet
    extra = 1    

@admin.register(TipoDeProblema)
class TipoDeProblemaAdmin(admin.ModelAdmin):
    '''Formulário para cadastro de um novo tipo de problema'''
    fields = ['descricao']

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    '''Formulário para cadastro de um endereço'''
    fields = [
        'logradouro',
        'numero',
        'complemento',
        'bairro',
        'cidade',
        'uf',
        'cep',
        'geolocalizacao',
    ]

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    '''Formulário para cadastro de um novo telefone'''
    fields = [
        'tipo',
        'ddd',
        'operadora',
        'numero',
    ]

@admin.register(LinkDeInternet)
class LinkDeInternet(admin.ModelAdmin):
    '''
    Formulário CRUD Link de Internet
    '''
    fields = [
        'escola',
        'fornecedor',
        'velocidade',
        'ip_circuito',
        'identificador',
        'local',
        'wifi',
        'cabo',
        'ativo',
        'funcionando',
    ]

    list_display = (
        'escola',
        'fornecedor',
        'velocidade',        
        'ip_circuito',
        'identificador',
        'local',
    )

    search_fields = [
        'escola',
        'fornecedor',
        'ip_circuito',
        'identificador',
    ]
    list_filter = [
        'escola',
        'fornecedor',
        'velocidade', 
        'wifi',
        'cabo',
    ]
    raw_id_fields = ('escola',)

@admin.register(Escola) 
class EscolaAdmin(admin.ModelAdmin):
    '''
    Formulário CRUD de escola.
    '''
    def gerarRelatorio(self, obj):
        '''Cria um botão para executar a view de impressão das informações do relatório
        Args:
            obj: um objeto do tipo Escola
        Returns:
            HttpResponseRedirect: reverse('reports:report_escola', args=(obj.designacao,))
        '''
        return HttpResponseRedirect(reverse('reports:report_escola', args=(obj.designacao,)))            
    
    gerarRelatorio.label = 'Gerar Relatório'
    gerarRelatorio.short_description = 'Gera um arquivo relatório da escola para impressão ou download'

    fields = [
        'designacao',
        'nome',
        'endereco',
        'telefones',
        'email',
        'locais',
        'ativo',
    ]

    list_display = (
        'designacao',
        'nome',
        'endereco',
    )
    inlines = [
        LinkDeInternetInLine, 
        ComputadorInLine
    ]

    search_fields = ['designacao', 'nome']
    
    raw_id_fields = ('locais',) 
    change_actions = ('gerarRelatorio', )

@admin.register(Computador)
class ComputadorAdmin(DjangoObjectActions, admin.ModelAdmin):
    '''
    Formulário para CRUD de um Computador
    '''

    fields = [
        'escola',
        'local',
        'tipo',
        'marca',
        'modelo',
        'numero_serie',
        'numero_inventario',
        'sistema_operacional',
        'processador',
        'ram',
        'hostname',
        'ip',
        'mac_address',
        'ativo',
        'funcionando',
    ]

    list_display = (
        'numero_serie',
        'numero_inventario',
        'tipo',
        'marca',
        'modelo',        
        'funcionando'
    )
    list_filter = ['tipo', 'marca', 'modelo']
    raw_id_fields = ('escola',)
    search_fields = ['tipo', 'marca', 'modelo', 'numero_serie', 'numero_inventario',]    

@admin.register(ParecerTecnico)
class ParecerTecnicoAdmin(DjangoObjectActions, admin.ModelAdmin):
    '''
    Formulário CRUD para Parecer Técnico de Baixa
    '''
    
    def gerarRelatorio(self, request, obj):
        '''Cria um botão para executar a view de impressão das informações do relatório
        Args:
            obj: um objeto do tipo ParecerTecnico
        Returns:
            HttpResponseRedirect: reverse('reports:report_parecer', args=(obj.id,))
        '''

        return HttpResponseRedirect(reverse('reports:report_parecer', args=(obj.id,)))            
    
    gerarRelatorio.label = 'Gerar Relatório'
    gerarRelatorio.short_description = 'Gera um arquivo do parecer técnico para impressão ou download'

    def save_model(self, request, obj, change):
        '''Registra o usuário que criou o relatório no momento de salvá-lo
        Args:
            request: requisição http
            obj: um objeto do tipo RatPadrao
            change: status de alteração no obj
        Returns:
            HttpResponseRedirect: reverse('reports:report_padrao', args=(obj.id,))
        '''
        if not change:            
            obj.tecnico = request.user
        obj.save()
    fieldsets = [
        (None, {'fields': ['escola', 'locais', 'chamados']}),        
    ]
    inlines = [BaixaInLine]
    list_display = (
        'escola',        
        'tecnico',
        'data_criacao',
        'recente'
    )
    
    list_filter = ['data_criacao','tecnico', 'escola']
    search_fields = ['escola', 'tecnico']
    date_hierarchy = 'data_criacao'
    raw_id_fields = ('escola',)
            
    change_actions = ('gerarRelatorio', )

@admin.register(RatLaboratorio)
class RatLaboratorioAdmin(DjangoObjectActions, admin.ModelAdmin):
    '''
    Formulário CRUD para Relatório de Antedimento de Laboratório
    '''
    
    def gerarRelatorio(self, request, obj):
        '''Cria um botão para executar a view de impressão das informações do relatório
        Args:
            obj: um objeto do tipo RatLaboratorio
        Returns:
            HttpResponseRedirect: reverse('reports:report_lab', args=(obj.id,))
        '''

        return HttpResponseRedirect(reverse('reports:report_lab', args=(obj.id,)))            

    gerarRelatorio.label = 'Gerar Relatório'
    gerarRelatorio.short_description = 'Gera um arquivo do parecer técnico para impressão ou download'

    def save_model(self, request, obj, change):
        '''Registra o usuário que criou o relatório no momento de salvá-lo
        Args:
            request: requisição http
            obj: um objeto do tipo RatPadrao
            change: status de alteração no obj
        Returns:
            HttpResponseRedirect: reverse('reports:report_padrao', args=(obj.id,))
        '''
        if not change:            
            obj.tecnico = request.user
        obj.save()
    fieldsets = [
        (None, {'fields': ['escola', 'locais', 'chamados']}),
        ('Laboratório', {'fields': ['tipo', 'fotos', 'computadores']}),
    ]    

    list_display = (
        'escola',        
        'tecnico',
        'data_criacao',
        'recente'
    )
    list_filter = ['data_criacao','tecnico', 'escola']    
    search_fields = ['escola', 'tecnico']    
    date_hierarchy = 'data_criacao'
    raw_id_fields = ('escola',)     
    filter_horizontal = ('computadores',)   
    change_actions = ('gerarRelatorio', )
    'links',
@admin.register(RatPadrao)
class RatPadraoAdmin(DjangoObjectActions, admin.ModelAdmin):
    '''
    Formulário CRUD para Relatório de Antedimento Técnico
    '''
    
    def gerarRelatorio(self, request, obj):
        '''Cria um botão para executar a view de impressão das informações do relatório
        Args:
            obj: um objeto do tipo RatPadrao
        Returns:
            HttpResponseRedirect: reverse('reports:report_padrao', args=(obj.id,))
        '''
    
        return HttpResponseRedirect(reverse('reports:report_padrao', args=(obj.id,)))            
    
    gerarRelatorio.label = 'Gerar Relatório'
    gerarRelatorio.short_description = 'Gera um arquivo da RAT para impressão ou download'

    def save_model(self, request, obj, change):
        '''Registra o usuário que criou o relatório no momento de salvá-lo
        Args:
            request: requisição http
            obj: um objeto do tipo RatPadrao
            change: status de alteração no obj
        Returns:
            HttpResponseRedirect: reverse('reports:report_padrao', args=(obj.id,))
        '''
        if not change:            
            obj.tecnico = request.user
        obj.save()

    fieldsets = [
        (None, {'fields': ['escola', 'locais', 'chamados']}),
        ('Descrição do Problema', {'fields': ['problemas', 'descricao']}),
        ('Solução do Problema', {'fields': ['solucao', 'recomendacao', 'itens_recomendados']}),        
    ]

    list_display = (
        'escola',
        'descricao',
        'tecnico',
        'data_criacao',
        'recente'
    )
    list_filter = ['data_criacao','tecnico']
    search_fields = ['designacao', 'tecnico']    
    date_hierarchy = 'data_criacao'
    raw_id_fields = ('escola',)
    change_actions = ('gerarRelatorio', )    

admin.site.register(FornecedorDeInternet)
admin.site.register(LocalDeAtendimento)
admin.site.register(TipoDeComputador)
admin.site.register(TipoDeLaboratorio)
admin.site.register(StatusDeBaixa)
admin.site.register(LinkDeLaboratorio)