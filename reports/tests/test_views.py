import pytest
from django.urls import resolve, reverse

from accounts.models import User
from reports.tests.factories import EscolaFactory, RatPadraoFactory, RatLaboratorioFactory, ParecerTecnicoFactory

pytestmark = pytest.mark.django_db

class RatPadraoViewsTests:
    def test_reverse_resolve(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)
        
        assert reverse('reports:rat_list') == '/rat/'
        assert resolve('/rat/').view_name ==  'reports:rat_list'
        
        url = reverse('reports:rat_lista_por_escola', kwargs={"designacao": "00.00.000"})
        assert url == '/rat/escola/00.00.000'
        
        view_name = resolve('/rat/escola/00.00.000').view_name
        assert view_name == 'reports:rat_lista_por_escola'
    
        url = reverse('reports:report_padrao', kwargs={"id": 1})
        assert url == '/rat/1/'
        
        view_name = resolve('/rat/1/').view_name
        assert view_name == 'reports:report_padrao'
    
    def test_status_code(self, client, escola):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        response = client.get(reverse('reports:rat_list'))
        assert response.status_code == 200

        response = client.get(
            reverse('reports:rat_lista_por_escola', kwargs={"designacao": escola.id})
        )
        assert response.status_code == 200
        
        ratpadrao = RatPadraoFactory()
        url = reverse('reports:report_padrao', kwargs={"id": ratpadrao.id})
        response = client.get(url)
        assert response.status_code == 200

class RatLaboratorioViewsTests:

    def test_reverse_resolve(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('reports:rat_lab_list') ==  '/rat-lab/'
        assert resolve('/rat-lab/').view_name ==  'reports:rat_lab_list'
        
        url = reverse('reports:rat_lab_lista_por_escola', kwargs={"designacao": "00.00.000"})
        assert url == '/rat-lab/escola/00.00.000'
        
        view_name = resolve('/rat-lab/escola/00.00.000').view_name
        assert view_name == 'reports:rat_lab_lista_por_escola'
    
        url = reverse('reports:report_lab', kwargs={"id": 1})
        assert url == '/rat/1/'
        
        view_name = resolve('/rat/1/').view_name
        assert view_name == 'reports:report_lab'       

    def test_status_code(self, client, escola):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        response = client.get(reverse('reports:rat_lab_list'))
        assert response.status_code == 200

        response = client.get(
            reverse('reports:rat_lab_lista_por_escola', kwargs={"designacao": escola.id})
        )
        assert response.status_code == 200
        
        ratlaboratorio = RatLaboratorioFactory()
        url = reverse('reports:report_padrao', kwargs={"id": ratlaboratorio.id})
        response = client.get(url)
        assert response.status_code == 200

class ParecerTecnicoViewsTests:

    def test_reverse_resolve(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('reports:parecer_list') ==  '/parecer/'
        assert resolve('/parecer/').view_name ==  'reports:parecer_list'

        url = reverse('reports:parecer_lista_por_escola', kwargs={"designacao": "00.00.000"})
        assert url == '/parecer/escola/00.00.000'
        
        view_name = resolve('/rat-lab/escola/00.00.000').view_name
        assert view_name == 'reports:parecer_lista_por_escola'
    
        url = reverse('reports:report_lab', kwargs={"id": 1})
        assert url == '/parecer/1/'
        
        view_name = resolve('/parecer/1/').view_name
        assert view_name == 'reports:report_parecer'
    
    def test_status_code(self, client, escola):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        response = client.get(reverse('reports:parecer_list'))
        assert response.status_code == 200

        response = client.get(
            reverse('reports:parecer_lista_por_escola', kwargs={"designacao": escola.id})
        )
        assert response.status_code == 200
    
        parecertecnico = ParecerTecnicoFactory()
        url = reverse('reports:report_parecer', kwargs={"id": parecertecnico.id})
        response = client.get(url)
        assert response.status_code == 200

class EscolaViewsTests:

    def test_reverse_resolve(self, client):   
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        assert reverse('reports:escola_list') == '/escola/' 
        assert resolve('/escola/').view_name ==  'reports:escola_list'

        url = reverse('reports:report_escola', kwargs={"id": "00.00.000"})
        assert url == '/escola/00.00.000/'
        
        view_name = resolve('/escola/00.00.000/').view_name
        assert view_name == 'reports:report_escola'

    def test_status_code(self, client):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)

        response = client.get(reverse('reports:escola_list'))
        assert response.status_code == 200
    
        escola = EscolaFactory()
        url = reverse('reports:report_parecer', kwargs={"id": escola.designacao})
        response = client.get(url)
        assert response.status_code == 200      