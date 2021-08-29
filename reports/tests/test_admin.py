from django.test import TestCase
from django.urls import reverse

import populate as populate
from accounts.models import User
from reports.serializers import *
from reports.models import *
from reports.views import *

'''
Este módulo define testes automatizados do sistema
'''

class SupportTables(TestCase):

    def setUp(self):   
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')        
        self.assertEqual(self.user.username, 'foobar')
        self.assertTrue(self.user.is_staff)
        self.client.force_login(user=self.user)
    
    def test_support_tables_admin_changelist(self):        
        data_serializers = [ 
            LocalDeAtendimentoSerializer, 
            TipoDeProblemaSerializer, 
            TipoDeComputadorSerializer, 
            TipoDeLaboratorioSerializer, 
            EnderecoSerializer, 
            FornecedorDeInternetSerializer,                                     
        ]
        log_filename = '/home/pi/Documents/sme/apps/ratPad/reports/tests/logs/loadFullDB.log'
        database_itens = populate.getFullDatabaseFrom(data_serializers, log_filename)
        for data_object in database_itens:                                   
            url = reverse(f"admin:reports_{data_object['name']}_changelist")
            response = self.client.get(url)
            self.assertIs(response.status_code, 200)
            
            url = reverse(f"admin:reports_{data_object['name']}_change", args=(data_object['result'].id,))
            response = self.client.get(url)
            self.assertIs(response.status_code, 200)
    
    def test_computador_change(self):
        self.client.force_login(user=self.user)
        local = populate.createObject(LocalDeAtendimentoSerializer, {"descricao": "Teste"})
        endereco_data = {
            "logradouro": "Rua A, 123",
            "numero": "120",
            "complemento": "Lt 10",
            "bairro": "Cruzeiro",
            "cidade": "Santa Cruz",
            "uf": "rj",
            "cep": "23078*-160",
            "geolocalizacao": "lt:44lg:14"
        }
        endereco = populate.createObject(EnderecoSerializer, endereco_data)
        escola_data = {
            "nome": "Abrigo no Antigo SESI / SENAI",
            "endereco": endereco.id,        
            "telefones": [],
            "email": "",            
            "locais": [local.id],
            "designacao": "10.11.107"
        }
        escola = populate.createObject(EscolaSerializer, escola_data)        
        tipo_computador = populate.createObject(TipoDeComputadorSerializer, {"descricao": "teste"})
        pc_data = {            
            "numero_serie": "123123ewXX",
            "escola": escola.designacao,
            "local": local.id,
            "tipo": tipo_computador.id,
            "marca": "Daten",
            "modelo": "DC1",
            "numero_inventario": "s335q4676tf",
            "sistema_operacional": "windowws 7",
            "processador": "3",
            "ram": "8",
            "hostname": "asd33",
            "ip": "127.0.0.1",
            "mac_address": "sadfasd32345",
        }
        pc = populate.createObject(ComputadorSerializer, pc_data)
        url = reverse('admin:reports_ratpadrao_change', args=(pc.numero_serie,))        
        response = self.client.get(url)
        print(response)        
        self.assertIs(response.status_code, 200)

    def test_escola_admin_change(self):
        local = populate.createObject(LocalDeAtendimentoSerializer, {"descricao": "Teste"})
        endereco_data = {
            "logradouro": "Rua A, 123",
            "numero": "120",
            "complemento": "Lt 10",
            "bairro": "Cruzeiro",
            "cidade": "Santa Cruz",
            "uf": "rj",
            "cep": "23078*-160",
            "geolocalizacao": "lt:44lg:14"
        }
        endereco = populate.createObject(EnderecoSerializer, endereco_data)
        escola_data = {
            "nome": "Abrigo no Antigo SESI / SENAI",
            "endereco": endereco.id,        
            "telefones": [],
            "email": "",            
            "locais": [local.id],
            "designacao": "10.11.007"
        }
        escola = populate.createObject(EscolaSerializer, escola_data)        
        url = reverse('admin:reports_ratpadrao_change', args=(escola.designacao,))        
        response = self.client.get(url)
        print(response)        
        self.assertIs(response.status_code, 200)

    def test_ratpadrao_admin_change(self):
        tipo_problema = populate.createObject(TipoDeProblemaSerializer, {"descricao": "Teste"})
        local = populate.createObject(LocalDeAtendimentoSerializer, {"descricao": "Teste"})
        endereco_data = {
            "logradouro": "Rua A, 123",
            "numero": "120",
            "complemento": "Lt 10",
            "bairro": "Cruzeiro",
            "cidade": "Santa Cruz",
            "uf": "rj",
            "cep": "23078*-160",
            "geolocalizacao": "lt:44lg:14"
        }
        endereco = populate.createObject(EnderecoSerializer, endereco_data)
        escola_data = {
            "nome": "Abrigo no Antigo SESI / SENAI",
            "endereco": endereco.id,        
            "telefones": [],
            "email": "",            
            "locais": [local.id],
            "designacao": "10.11.008"
        }
        escola = populate.createObject(EscolaSerializer, escola_data)
        rat_data = {
            "escola": escola.designacao,
            "chamados": "1664151",
            "tecnico": self.user.id,            
            "locais": [local.id],
            "descricao": "Configura\u00e7\u00e3o de Modem da Oi",
            "solucao": "Ap\u00f3s visita t\u00e9cnica da operadora a diretoria da unidade solicittou verifica\u00e7\u00e3o do sinal de internet e configura\u00e7\u00e3o da rede interna com o link da Oi e da Embratel simultaneamente para dividir a banda de aceeso. Efetuado teste de velocidade pelo site speedtest ookla aferindo velociadade de download de 8,56 Mbps. O modem da Oi foi conecetado exclusivamente no AP do projeto escola conectada.",
            "recomendacao": False,
            "itens_recomendados": "None",
            "problemas": [tipo_problema.id]
        }
        
        rat = populate.createObject(RatPadraoSerializer, rat_data)        
        url = reverse('admin:reports_ratpadrao_change', args=(rat.id,))        
        response = self.client.get(url)
        self.assertIs(response.status_code, 200)
  
    def test_ratlaboratorio_admin_change(self):
        
        local = populate.createObject(LocalDeAtendimentoSerializer, {"descricao": "Teste"})
        endereco_data = {
            "logradouro": "Rua A, 123",
            "numero": "120",
            "complemento": "Lt 10",
            "bairro": "Cruzeiro",
            "cidade": "Santa Cruz",
            "uf": "rj",
            "cep": "23078*-160",
            "geolocalizacao": "lt:44lg:14"
        }
        endereco = populate.createObject(EnderecoSerializer, endereco_data)
        escola_data = {
            "nome": "Abrigo no Antigo SESI / SENAI",
            "endereco": endereco.id,        
            "telefones": [],
            "email": "",            
            "locais": [local.id],
            "designacao": "10.11.009"
        }
        escola = populate.createObject(EscolaSerializer, escola_data)
        fornecedor_data = {
            "nome": "Oi",
            "telefone": [],
            "link_chamado": "http://www.oi.com.br/chamado",  
        }
        fornecedor = populate.createObject(FornecedorDeInternetSerializer, fornecedor_data)
        link_data = {
            "escola":escola.designacao,
            "fornecedor":fornecedor.id,
            "velocidade":10,
            "ip_circuito":"189.0.0.2",
            "identificador":"RJO/IP/2000",
            "local":local.id  
        }
        link = populate.createObject(LinkDeInternetSerializer, link_data)
        tipo_computador = populate.createObject(TipoDeComputadorSerializer, {"descricao": "teste"})
        pc_data = {            
            "numero_serie": "123123ewXX",
            "escola": escola.designacao,
            "local": local.id,
            "tipo": tipo_computador.id,
            "marca": "Daten",
            "modelo": "DC1",
            "numero_inventario": "s335q4676tf",
            "sistema_operacional": "windowws 7",
            "processador": "3",
            "ram": "8",
            "hostname": "asd33",
            "ip": "127.0.0.1",
            "mac_address": "sadfasd32345",
        }
        pc = populate.createObject(ComputadorSerializer, pc_data)
        tipo_laboratorio = populate.createObject(TipoDeLaboratorioSerializer, {"descricao": "teste"})
        ratlab_data = {
            "escola": escola.designacao,
            "chamados": "1664151",
            "tecnico": self.user.id,            
            "locais": [local.id],
            "tipo":tipo_laboratorio.id,            
            "links": [link.id],
            "computadores": [pc.numero_serie],                        
        }
                
        rat_lab = populate.createObject(RatLaboratorioSerializer, ratlab_data)
        url = reverse('admin:reports_ratlaboratorio_change', args=(rat_lab.id,))        
        response = self.client.get(url)
        self.assertIs(response.status_code, 200)

    def test_parecer_admin_change(self):
        local = populate.createObject(LocalDeAtendimentoSerializer, {"descricao": "Teste"})
        endereco_data = {
            "logradouro": "Rua A, 123",
            "numero": "120",
            "complemento": "Lt 10",
            "bairro": "Cruzeiro",
            "cidade": "Santa Cruz",
            "uf": "rj",
            "cep": "23078*-160",
            "geolocalizacao": "lt:44lg:14"
        }
        endereco = populate.createObject(EnderecoSerializer, endereco_data)
        escola_data = {
            "nome": "Abrigo no Antigo SESI / SENAI",
            "endereco": endereco.id,        
            "telefones": [],
            "email": "",            
            "locais": [local.id],
            "designacao": "10.11.009"
        }
        escola = populate.createObject(EscolaSerializer, escola_data)
        parecer_data = {
            "escola": escola.designacao,
            "chamados": "1664151",
            "tecnico": self.user.id,
            "data_criacao": "2021-06-16T06:00:00Z",
            "data_edicao": "2021-07-25T22:17:57.364Z",
            "locais": [local.id]
        }
        
        parecer = populate.createObject(ParecerTecnicoSerializer, parecer_data) 
        url = reverse('admin:reports_ratlaboratorio_change', args=(parecer.id,))        
        response = self.client.get(url)
        print(response)        
        self.assertIs(response.status_code, 200)
    
    def teste_baixa_admin_change(self):
        local = populate.createObject(LocalDeAtendimentoSerializer, {"descricao": "Teste"})
        endereco_data = {
            "logradouro": "Rua A, 123",
            "numero": "120",
            "complemento": "Lt 10",
            "bairro": "Cruzeiro",
            "cidade": "Santa Cruz",
            "uf": "rj",
            "cep": "23078*-160",
            "geolocalizacao": "lt:44lg:14"
        }
        endereco = populate.createObject(EnderecoSerializer, endereco_data)
        escola_data = {
            "nome": "Abrigo no Antigo SESI / SENAI",
            "endereco": endereco.id,        
            "telefones": [],
            "email": "",            
            "locais": [local.id],
            "designacao": "10.11.008"
        }
        escola = populate.createObject(EscolaSerializer, escola_data)
        parecer_data = {
            "escola": escola.designacao,
            "chamados": "1664151",
            "tecnico": self.user.id,
            "data_criacao": "2021-06-16T06:00:00Z",
            "data_edicao": "2021-07-25T22:17:57.364Z",
            "locais": [local.id]
        }        
        parecer = populate.createObject(ParecerTecnicoSerializer, parecer_data)        
        tipo_computador = populate.createObject(TipoDeComputadorSerializer, {"descricao": "teste"})
        pc_data = {            
            "numero_serie": "123123ewRR",
            "escola": escola.designacao,
            "local": local.id,
            "tipo": tipo_computador.id,
            "marca": "Daten",
            "modelo": "DC1",
            "numero_inventario": "s335q4676tf",
            "sistema_operacional": "windowws 7",
            "processador": "3",
            "ram": "8",
            "hostname": "asd33",
            "ip": "127.0.0.1",
            "mac_address": "sadfasd32345",
        }
        pc = populate.createObject(ComputadorSerializer, pc_data)
        baixa_data = {
            "parecer": parecer.id,
            "computador": pc.numero_serie,
            "motivo": "obsolesc\u00eancia",
            "descricao": "N\u00e3o liga"
        }
        baixa = populate.createObject(StatusDeBaixaSerializer, baixa_data)
        url = reverse('admin:reports_statusdebaixa_change', args=(baixa.id,))        
        response = self.client.get(url)
        self.assertIs(response.status_code, 200)