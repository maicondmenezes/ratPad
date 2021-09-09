from django.urls import path, re_path
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

    path('escola-autocomplete/', EscolaAutocomplete.as_view(), name='escola_autocomplete'),    
    path('local-autocomplete/', LocalDeAtendimentoAutocomplete.as_view(), name='local_autocomplete'),   
]