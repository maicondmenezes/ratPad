from django.urls import path, re_path
from reports.views import RatPadraoDetailView, RatPadraoListView, RatLaboratorioListView, ParecerTecnicoListView, EscolaListView, RatPadraoCreateView
from reports.views import report, reportLab, reportParecer, reportEscola, systemInfo

'''Módulo responságel por gerenciar os padrões de URLS disponíveis no sistema'''

app_name = 'reports'

urlpatterns = [    
    path('rat/',  RatPadraoListView.as_view() , name='rat_list'),
    path('rat/<int:pk>', RatPadraoDetailView.as_view(), name='rat_detail'),
    path('rat/add/',  RatPadraoCreateView.as_view() , name='rat_add'),
    path('rat/edit/<int:pk>',  RatPadraoCreateView.as_view() , name='rat_edit'),
    path('rat/delete/<int:pk>',  RatPadraoCreateView.as_view() , name='rat_del'),
    re_path(r'^rat/([0-9]{2}\.[0-9]{2}\.[0-9]{3})?$', RatPadraoListView.as_view(), name='rat_list_por_escola'),    
    
        
    path('rat-lab/', RatLaboratorioListView.as_view(), name='rat_lab_list'),    
    re_path(r'^rat-lab/([0-9]{2}\.[0-9]{2}\.[0-9]{3})?$', RatLaboratorioListView.as_view(), name='rat_lab_list_por_escola'),
    path('rat-lab/<int:ratlaboratorio_id>', reportLab, name='report_lab'),

    path('parecer/', ParecerTecnicoListView.as_view(), name='parecer_list'),
    re_path(r'^parecer/([0-9]{2}\.[0-9]{2}\.[0-9]{3})?$', ParecerTecnicoListView.as_view(), name='parecer_list_por_escola'),
    path('parecer/<int:parecertecnico_id>', reportParecer, name='report_parecer'),
    
    path('escola/', EscolaListView.as_view(), name='escola_list'),
    re_path(r'^escola/([0-9]{2}\.[0-9]{2}\.[0-9]{3})?$', reportEscola, name='report_escola'),
    path('info/', systemInfo, name='system_info'),
]