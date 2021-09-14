from django.urls import path
from reports.views import *

'''Módulo responságel por gerenciar os padrões de URLS disponíveis no sistema'''

app_name = 'reports'

urlpatterns = [
    path('escola/',  EscolaListView.as_view() , name='escola_list'), 
    path('escola/<slug:slug>', EscolaDetailView.as_view(), name='escola_detail'),
    path('escola/add/',  EscolaCreateView.as_view() , name='escola_add'),        
    path('escola/edit/<slug:slug>',  EscolaUpdateView.as_view() , name='escola_edit'),
    path('escola/delete/<slug:slug>',  EscolaDeleteView.as_view() , name='escola_del'),  

    path('rat/',  RatPadraoListView.as_view() , name='rat_list'),
    path('rat/<int:pk>', RatPadraoDetailView.as_view(), name='rat_detail'),
    path('rat/add/',  RatPadraoCreateView.as_view() , name='rat_add'),
    path('rat/edit/<int:pk>',  RatPadraoUpdateView.as_view() , name='rat_edit'),
    path('rat/delete/<int:pk>',  RatPadraoDeleteView.as_view() , name='rat_del'),
    path('rat/escola/<slug:slug>', RatPadraoListView.as_view(), name='rat_list_por_escola'), 

    path('rat-laboratorio/',  RatLaboratorioListView.as_view() , name='ratlab_list'),
    path('rat-laboratorio/<int:pk>', RatLaboratorioDetailView.as_view(), name='ratlab_detail'),
    path('rat-laboratorio/add/',  RatLaboratorioCreateView.as_view() , name='ratlab_add'),
    path('rat-laboratorio/edit/<int:pk>',  RatLaboratorioUpdateView.as_view() , name='ratlab_edit'),
    path('rat-laboratorio/delete/<int:pk>',  RatLaboratorioDeleteView.as_view() , name='ratlab_del'),
    path('rat-laboratorio/escola/<slug:slug>', RatLaboratorioListView.as_view(), name='ratlab_list_por_escola'),     
    path('ajax/ativos-escola/', load_assets, name='ajax_load_assets'),

    path('parecer-tecnico/',  ParecerTecnicoListView.as_view() , name='parecer_list'),
    path('parecer-tecnico/<int:pk>', ParecerTecnicoDetailView.as_view(), name='parecer_detail'),
    path('parecer-tecnico/add/',  ParecerTecnicoCreateView.as_view() , name='parecer_add'),
    path('parecer-tecnico/edit/<int:pk>',  ParecerTecnicoUpdateView.as_view() , name='parecer_edit'),
    path('parecer-tecnico/delete/<int:pk>',  ParecerTecnicoDeleteView.as_view() , name='parecer_del'),
    path('parecer-tecnico/escola/<slug:slug>', ParecerTecnicoListView.as_view(), name='parecer_list_por_escola'),     
    path('ajax/computadores/', load_computers, name='ajax_load_computers'),

    path('computador-autocomplete/', ComputadorAutocomplete.as_view(), name='computador_autocomplete'),    
    path('escola-autocomplete/', EscolaAutocomplete.as_view(), name='escola_autocomplete'),    
    path('local-autocomplete/', LocalDeAtendimentoAutocomplete.as_view(), name='local_autocomplete'),   
]