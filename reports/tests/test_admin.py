import pytest
from django.urls import resolve, reverse

from accounts.models import User
from reports.models import *
from reports.views import *
from reports.tests.factories import *

class LocalDeAtendimentoAdminTest:
    
    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_localdeatendimento_changelist') == '/admin/reports/localdeatendimento/'
        assert resolve('/admin/reports/localdeatendimento/').view_name ==  'admin:reports_localdeatendimento_changelist'
        
        response = client.get('/admin/reports/localdeatendimento/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_localdeatendimento_change', kwargs={"id": 1})        
        assert url == '/admin/reports/localdeatendimento/1/change/'
        
        view_name = resolve('/admin/reports/localdeatendimento/1/change/').view_name
        assert view_name == 'admin:reports_localdeatendimento_change'

        localdeatendimento = LocalDeAtendimentoFactory()
        url = reverse('admin:reports_localdeatendimento_change', kwargs={"id": localdeatendimento.id})
        
        response = client.get(url)
        assert response.status_code == 200        

class TipoDeProblemaAdminTest:
    
    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_tipodeproblema_changelist') == '/admin/reports/tipodeproblema/'
        assert resolve('/admin/reports/tipodeproblema/').view_name ==  'admin:reports_tipodeproblema_changelist'
        
        response = client.get('/admin/reports/tipodeproblema/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_tipodeproblema_change', kwargs={"id": 1})        
        assert url == '/admin/reports/tipodeproblema/1/change/'
        
        view_name = resolve('/admin/reports/tipodeproblema/1/change/').view_name
        assert view_name == 'admin:report_tipodeproblema_change'

        tipodeproblema = TipoDeProblemaFactory()
        url = reverse('admin:report_tipodeproblema_change', kwargs={"id": tipodeproblema.id})
        
        response = client.get(url)
        assert response.status_code == 200        

class TipoDeComputadorAdminTest:
    
    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_tipodecomputador_changelist') == '/admin/reports/tipodecomputador/'
        assert resolve('/admin/reports/tipodecomputador/').view_name ==  'admin:reports_tipodecomputador_changelist'
        
        response = client.get('/admin/reports/tipodecomputador/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_tipodecomputador_change', kwargs={"id": 1})        
        assert url == '/admin/reports/tipodecomputador/1/change/'
        
        view_name = resolve('/admin/reports/tipodecomputador/1/change/').view_name
        assert view_name == 'admin:reports_tipodecomputador_change'

        tipodecomputador = TipoDeComputadorFactory()
        url = reverse('admin:reports_tipodecomputador_change', kwargs={"id": tipodecomputador.id})
        
        response = client.get(url)
        assert response.status_code == 200

class TipoDeLaboratorioAdminTest:
    
    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_tipodelaboratorio_changelist') == '/admin/reports/tipodelaboratorio/'
        assert resolve('/admin/reports/tipodelaboratorio/').view_name ==  'admin:reports_tipodelaboratorio_changelist'
        
        response = client.get('/admin/reports/tipodelaboratorio/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_tipodelaboratorio_change', kwargs={"id": 1})        
        assert url == '/admin/reports/tipodelaboratorio/1/change/'
        
        view_name = resolve('/admin/reports/tipodelaboratorio/1/change/').view_name
        assert view_name == 'admin:reports_tipodelaboratorio_change'

        tipodelaboratorio = TipoDeLaboratorioFactory()
        url = reverse('reports:report_padrao', kwargs={"id": tipodelaboratorio.id})
        
        response = client.get(url)
        assert response.status_code == 200

class EnderecoAdminTest:

    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_endereco_changelist') == '/admin/reports/endereco/'
        assert resolve('/admin/reports/endereco/').view_name ==  'admin:reports_endereco_changelist'
        
        response = client.get('/admin/reports/endereco/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_endereco_change', kwargs={"id": 1})        
        assert url == '/admin/reports/endereco/1/change/'
        
        view_name = resolve('/admin/reports/endereco/1/change/').view_name
        assert view_name == 'admin:reports_endereco_change'

        endereco = EnderecoFactory()
        url = reverse('reports:report_padrao', kwargs={"id": endereco.id})
        
        response = client.get(url)
        assert response.status_code == 200

class FornecedorDeInternetAdminTest:
    
    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_fornecedordeinternet_changelist') == '/admin/reports/fornecedordeinternet/'
        assert resolve('/admin/reports/fornecedordeinternet/').view_name ==  'admin:reports_fornecedordeinternet_changelist'
        
        response = client.get('/admin/reports/fornecedordeinternet/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_fornecedordeinternet_change', kwargs={"id": 1})        
        assert url == '/admin/reports/fornecedordeinternet/1/change/'
        
        view_name = resolve('/admin/reports/fornecedordeinternet/1/change/').view_name
        assert view_name == 'admin:reports_fornecedordeinternet_change'

        fornecedordeinternet = FornecedorDeInternetFactory()
        url = reverse('reports:report_padrao', kwargs={"id": fornecedordeinternet.id})
        
        response = client.get(url)
        assert response.status_code == 200

class EscolaAdminTest:

    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_escola_changelist') == '/admin/reports/escola/'
        assert resolve('/admin/reports/escola/').view_name ==  'admin:reports_escola_changelist'
        
        response = client.get('/admin/reports/escola/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_escola_change', kwargs={"id": 1})        
        assert url == '/admin/reports/escola/1/change/'
        
        view_name = resolve('/admin/reports/escola/1/change/').view_name
        assert view_name == 'admin:reports_escola_change'

        escola = EscolaFactory()
        url = reverse('reports:report_padrao', kwargs={"id": escola.id})
        
        response = client.get(url)
        assert response.status_code == 200        
        
class LinkDeInternetAdminTest:

    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_linkdeinternet_changelist') == '/admin/reports/linkdeinternet/'
        assert resolve('/admin/reports/linkdeinternet/').view_name ==  'admin:reports_linkdeinternet_changelist'
        
        response = client.get('/admin/reports/linkdeinternet/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_linkdeinternet_change', kwargs={"id": 1})        
        assert url == '/admin/reports/linkdeinternet/1/change/'
        
        view_name = resolve('/admin/reports/linkdeinternet/1/change/').view_name
        assert view_name == 'admin:reports_linkdeinternet_change'

        linkdeinternet = LinkDeInternetFactory()
        url = reverse('reports:report_padrao', kwargs={"id": linkdeinternet.id})
        
        response = client.get(url)
        assert response.status_code == 200
        
        
class RatPadraoAdminTest:

    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_ratpadrao_changelist') == '/admin/reports/ratpadrao/'
        assert resolve('/admin/reports/ratpadrao/').view_name ==  'admin:reports_ratpadrao_changelist'
        
        response = client.get('/admin/reports/ratpadrao/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_ratpadrao_change', kwargs={"id": 1})        
        assert url == '/admin/reports/ratpadrao/1/change/'
        
        view_name = resolve('/admin/reports/ratpadrao/1/change/').view_name
        assert view_name == 'admin:reports_ratpadrao_change'

        ratpadrao = RatPadraoFactory()
        ratpadrao['tecnico'] = user.id
        url = reverse('reports:report_padrao', kwargs={"id": ratpadrao.id})
        
        response = client.get(url)
        assert response.status_code == 200
                
class ComputadorAdminTest:

    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_computador_changelist') == '/admin/reports/computador/'
        assert resolve('/admin/reports/computador/').view_name ==  'admin:reports_computador_changelist'
        
        response = client.get('/admin/reports/computador/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_computador_change', kwargs={"id": 1})        
        assert url == '/admin/reports/computador/1/change/'
        
        view_name = resolve('/admin/reports/computador/1/change/').view_name
        assert view_name == 'admin:reports_computador_change'

        computador = ComputadorFactory()
        url = reverse('reports:report_padrao', kwargs={"id": computador.id})
        
        response = client.get(url)
        assert response.status_code == 200       
        
class RatLaboratorioAdminTest:

    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_ratlaboratorio_changelist') == '/admin/reports/ratlaboratorio/'
        assert resolve('/admin/reports/ratlaboratorio/').view_name ==  'admin:reports_ratlaboratorio_changelist'
        
        response = client.get('/admin/reports/ratlaboratorio/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_ratlaboratorio_change', kwargs={"id": 1})        
        assert url == '/admin/reports/ratlaboratorio/1/change/'
        
        view_name = resolve('/admin/reports/ratlaboratorio/1/change/').view_name
        assert view_name == 'admin:reports_ratlaboratorio_change'

        ratlaboratorio = RatLaboratorioFactory()
        ratlaboratorio['tecnico'] = user.id
        url = reverse('reports:report_padrao', kwargs={"id": ratlaboratorio.id})
        
        response = client.get(url)
        assert response.status_code == 200
        
        
class ParecerTecnicoAdminTest:

    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_parecertecnico_changelist') == '/admin/reports/parecertecnico/'
        assert resolve('/admin/reports/parecertecnico/').view_name ==  'admin:reports_parecertecnico_changelist'
        
        response = client.get('/admin/reports/parecertecnico/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_parecertecnico_change', kwargs={"id": 1})        
        assert url == '/admin/reports/parecertecnico/1/change/'
        
        view_name = resolve('/admin/reports/parecertecnico/1/change/').view_name
        assert view_name == 'admin:reports_parecertecnico_change'

        parecertecnico = ParecerTecnicoFactory()
        parecertecnico['tecnico'] = user.id
        url = reverse('reports:report_padrao', kwargs={"id": parecertecnico.id})
        
        response = client.get(url)
        assert response.status_code == 200        
        
class StatusDeBaixaAdminTest:

    def test_changelist(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('admin:reports_statusdebaixa_changelist') == '/admin/reports/statusdebaixa/'
        assert resolve('/admin/reports/statusdebaixa/').view_name ==  'admin:reports_statusdebaixa_changelist'
        
        response = client.get('/admin/reports/statusdebaixa/')
        assert response.status_code == 200
            
    def test_change(self, client):        
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        url = reverse('admin:reports_statusdebaixa_change', kwargs={"id": 1})        
        assert url == '/admin/reports/statusdebaixa/1/change/'
        
        view_name = resolve('/admin/reports/statusdebaixa/1/change/').view_name
        assert view_name == 'admin:reports_statusdebaixa_change'

        statusdebaixa = StatusDeBaixaFactory()
        url = reverse('admin:reports_statusdebaixa_change', kwargs={"id": statusdebaixa.id})
        
        response = client.get(url)
        assert response.status_code == 200