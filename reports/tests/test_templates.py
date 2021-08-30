import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

from accounts.models import User
from reports.tests.factories import RatPadraoFactory, RatLaboratorioFactory, ParecerTecnicoFactory

pytestmark = pytest.mark.django_db

class RatPadraoTemplatesTests:
    def test_templates(self, client, escola):
        username = "user1"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)  
        
        response = client.get(reverse('reports:rat_list'))
        assertTemplateUsed( response, 'reports/ratpadrao_list.html')
        
        response = client.get(
            reverse('reports:rat_lista_por_escola', kwargs={"designacao": escola.id})
        )        
        assertTemplateUsed (response, 'reports/ratpadrao_list.html')
        
        ratpadrao = RatPadraoFactory()
        url = reverse('reports:report_padrao', kwargs={"id": ratpadrao.id})
        response = client.get(url)
        assertTemplateUsed (response, 'reports/report_padrao.html')

class RatLaboratorioTemplatesTests:
    def test_templates(self, client, escola):
        username = "user2"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)  
        
        response = client.get(reverse('reports:rat_lab_list'))
        assertTemplateUsed( response, 'reports/ratlaboratorio_list.html')
        
        response = client.get(
            reverse('reports:rat_lab_lista_por_escola', kwargs={"designacao": escola.id})
        )        
        assertTemplateUsed (response, 'reports/ratlaboratorio_list.html')
        
        ratlaboratorio = RatLaboratorioFactory()
        url = reverse('reports:report_laboratorio', kwargs={"id": ratlaboratorio.id})
        response = client.get(url)
        assertTemplateUsed (response, 'reports/report_laboratorio.html')    

class ParecerTecnicoTemplatesTests:
    def test_templates(self, client, escola):
        username = "user3"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)  
        
        response = client.get(reverse('reports:parecer_list'))
        assertTemplateUsed( response, 'reports/parecertecnico_list.html')
        
        response = client.get(
            reverse('reports:parecer_lista_por_escola', kwargs={"designacao": escola.id})
        )        
        assertTemplateUsed (response, 'reports/parecertecnico_list.html')
        
        parecertecnico = ParecerTecnicoFactory()
        url = reverse('reports:report_parecer', kwargs={"id": parecertecnico.id})
        response = client.get(url)
        assertTemplateUsed (response, 'reports/report_parecer.html')
    
class EscolaTemplatesTests:
    def test_templates(self, client, escola):
        username = "user4"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        client.force_login(user)  
        
        response = client.get(reverse('reports:escola_list'))
        assertTemplateUsed( response, 'reports/escola_list.html')
        
        ratpadrao = RatPadraoFactory()
        url = reverse('reports:report_escola', kwargs={"id": ratpadrao.id})
        response = client.get(url)
        assertTemplateUsed (response, 'reports/report_escola.html')
    
   