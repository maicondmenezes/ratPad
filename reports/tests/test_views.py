from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from populate import *
from reports.models import *
from reports.views import *
from reports.serializers import *

'''
Este módulo define testes automatizados do sistema
'''

class ReportsViewsTests(TestCase):
    def test_rever_resolve(self):
        response = self.client.get(reverse('reports:rat_list'))
        response = self.client.get(resolve('reports:rat_list'))
        
        response = self.client.get(reverse('reports:rat_list_por_escola'))
        response = self.client.get(resolve('reports:rat_list_por_escola'))
        
        response = self.client.get(reverse('reports:report_padrao'))
        response = self.client.get(resolve('reports:report_padrao'))
        
        response = self.client.get(reverse('reports:rat_lab_list'))
        response = self.client.get(resolve('reports:rat_lab_list'))
        
        response = self.client.get(reverse('reports:rat_lab_list_por_escola'))
        response = self.client.get(resolve('reports:rat_lab_list_por_escola'))
        
        response = self.client.get(reverse('reports:report_lab'))
        response = self.client.get(resolve('reports:report_lab'))
        
        response = self.client.get(reverse('reports:parecer_list'))
        response = self.client.get(resolve('reports:parecer_list'))
        
        response = self.client.get(reverse('reports:parecer_list_por_escola'))
        response = self.client.get(resolve('reports:parecer_list_por_escola'))
        
        response = self.client.get(reverse('reports:report_parecer'))
        response = self.client.get(resolve('reports:report_parecer'))
        
        response = self.client.get(reverse('reports:escola_list'))
        response = self.client.get(resolve('reports:escola_list'))
        
        response = self.client.get(reverse('reports:report_escola'))
        response = self.client.get(resolve('reports:report_escola'))
        
    def test_templates(self):
        response = self.client.get(reverse('reports:rat_list'))
        self.assertTemplateUsed(response,'ratpadrao_list.html')
        
        response = self.client.get(reverse('reports:rat_list_por_escola'))
        self.assertTemplateUsed(response,'ratpadrao_list.html')
        
        response = self.client.get(reverse('reports:report_padrao'))
        self.assertTemplateUsed(response,'report_padrao.html')
        
        response = self.client.get(reverse('reports:rat_lab_list'))
        self.assertTemplateUsed(response,'ratlaboratorio_list.html')
        
        response = self.client.get(reverse('reports:rat_lab_list_por_escola'))
        self.assertTemplateUsed(response,'ratlaboratorio_list.html')
        
        response = self.client.get(reverse('reports:report_lab'))
        self.assertTemplateUsed(response,'report_lab.html')
        
        response = self.client.get(reverse('reports:parecer_list'))
        self.assertTemplateUsed(response,'parecertecnico_list.html')
        
        response = self.client.get(reverse('reports:parecer_list_por_escola'))
        self.assertTemplateUsed(response,'parecertecnico_list.html')
        
        response = self.client.get(reverse('reports:report_parecer'))
        self.assertTemplateUsed(response,'report_parecer.html')
        
        response = self.client.get(reverse('reports:escola_list'))
        self.assertTemplateUsed(response,'escola_list.html')
        
        response = self.client.get(reverse('reports:report_escola'))
        self.assertTemplateUsed(response,'report_escola.html')   
        