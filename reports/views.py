from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets

from reports.models import ParecerTecnico, RatPadrao, RatLaboratorio, Escola, Computador
from reports.serializers import ComputadorSerializer



'''
Este módulo define as seleções de dados para vizualização dos usuários.
Em geral os dados obtidos são enviados via função render(), para um template HTML, junto com o(s) objeto(s) recuperado e a requisição HTTP'''

class RatPadraoCreateView(CreateView):
    model = RatPadrao
    template_name = 'reports/ratpadrao/add.html'    
    fields = '__all__'

class RatPadraoUpdateView(UpdateView):
    model = RatPadrao
    template_name = 'reports/ratpadrao/edit.html'
    context_object_name = 'rat'
    fields = '__all__'
class RatPadraoDetailView(DetailView):
    model = RatPadrao
    template_name = 'reports/ratpadrao/detail.html'
    context_object_name = 'rat'    

class RatPadraoListView(ListView):
    model = RatPadrao
    context_object_name = 'rats'
    template_name = 'reports/ratpadrao/list.html'
    escola = None        
        
    def get_queryset(self):                
        queryset = RatPadrao.objects.all()

        escola_designacao = self.kwargs.get('designacao')
        if escola_designacao:
            self.escola = get_object_or_404(Escola, designacao=escola_designacao)
            queryset = queryset.filter(escola=self.escola)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['escola'] = self.escola
        context['escolas']= Escola.ativos.all()
        return context

class RatPadraoDeleteView(DeleteView):
    model = RatPadrao
    template_name = 'reports/ratpadrao/delete.html'
    context_object_name = 'rat'
    fields = '__all__'

class RatLaboratorioListView(ListView):
    escola = None
    paginate_by = 20
    
    def get_queryset(self):        
        queryset = RatLaboratorio.objects.all()

        escola_designacao = self.kwargs.get('designacao')
        if escola_designacao:
            self.escola = get_object_or_404(Escola, designacao=escola_designacao)
            queryset = queryset.filter(escola=self.escola)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['escola'] = self.escola
        context['escolas']= Escola.ativos.all()
        return context

class ParecerTecnicoListView(ListView):
    escola = None
    paginate_by = 20
    
    def get_queryset(self):        
        queryset = ParecerTecnico.objects.all()

        escola_designacao = self.kwargs.get('designacao')
        if escola_designacao:
            self.escola = get_object_or_404(Escola, designacao=escola_designacao)
            queryset = queryset.filter(escola=self.escola)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['escola'] = self.escola
        context['escolas']= Escola.ativos.all()
        return context

class EscolaListView(ListView):
    paginate_by = 20

    def get_queryset(self):
        queryset = Escola.ativos.all()
        
        return queryset
    
@login_required
def report(request, ratpadrao_id):
    '''Vizualização dos dados de um único Relatório de Atendimento Técnico, exige login no sistema para acessar.

        Args:
            request (obj): uma requisição http
            ratpadrao_id (int): identificador do relatorio

        Raises:
            Http404: Esta RAT não existe

        Returns:
            render: (request, 'reports/docs/report_padrao.html', {'rat' : rat})
    '''
    try:
        rat = RatPadrao.objects.get(pk=ratpadrao_id)
    except RatPadrao.DoesNotExist:
        raise Http404('Esta RAT não existe')
    return render(request, 'reports/docs/report_padrao.html', {'rat' : rat})

@login_required
def reportEscola(request, escola_designacao):
    '''Vizualização dos dados de uma única Escola, exige login no sistema para acessar.

        Args:
            request (obj): uma requisição http
            escola_id (int): identificador da Escola

        Raises:
            Http404: Esta escola não existe

        Returns:
            render: (request, 'reports/docs/report_escola.html', {'escola' : escola})
    '''
    try:
        escola = Escola.objects.get(designacao=escola_designacao)
    except Escola.DoesNotExist:
        raise Http404('Esta escola não existe')
    return render(request, 'reports/docs/report_escola.html', {'escola' : escola})

@login_required
def reportLab(request, ratlaboratorio_id):
    '''Vizualização dos dados de um único Relatório de Atendimento de Laboratório, exige login no sistema para acessar.

        Args:
            request (obj): uma requisição http
            ratlaboratorio_id (int): identificador do Relatório de Atendimento de Laboratório

        Raises:
            Http404: Esta RAT não existe

        Returns:
            render: (request, 'reports/docs/report_lab.html', {'rat_lab' : rat_lab})
    '''
    try:
        rat_lab = RatLaboratorio.objects.get(pk=ratlaboratorio_id)
    except RatLaboratorio.DoesNotExist:
        raise Http404('Esta RAT não existe')
    return render(request, 'reports/docs/report_lab.html', {'rat_lab' : rat_lab})

@login_required
def reportParecer(request, parecertecnico_id):
    '''Vizualização dos dados de um único PArecer Técnico de Baiza, exige login no sistema para acessar.

        Args:
            request (obj): uma requisição http
            parecertecnico_id (int): identificador do Parecer Técnico de Baixa

        Raises:
            Http404: Esta RAT não existe

        Returns:
            render: (request, 'reports/docs/report_lab.html', {'rat_lab' : rat_lab})
    '''
    try:
        rat_parecer = ParecerTecnico.objects.get(pk=parecertecnico_id)
    except ParecerTecnico.DoesNotExist:
        raise Http404('Este Parecer não existe')
    return render(request, 'reports/docs/report_parecer.html', {'rat_parecer' : rat_parecer})

@login_required
def systemInfo(request):    
    '''Vizualização de uma página para download do aplicativo ratPad Asset Manager.

        Args:
            request (obj): uma requisição http            

        Returns:
            render: ( request, 'reports/logs/system_info.html')
    '''

    return render( request, 'reports/logs/system_info.html')

class ComputadorViewset(viewsets.ModelViewSet):
    '''Conjunto de seleções de dados para interagir com a api rest gerada pelo django-rest-framework.'''
    
    queryset = Computador.objects.all()
    serializer_class = ComputadorSerializer