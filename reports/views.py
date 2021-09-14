from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from dal import autocomplete
from rest_framework import viewsets

from reports.models import ParecerTecnico, Escola, LinkDeInternet, RatPadrao, RatLaboratorio, Computador, LocalDeAtendimento
from reports.forms import StatusDeBaixaInlineForm, ComputadorInlineForm, LinkDeInternetInlineForm, LinkDeLaboratorioInlineForm, RatPadraoCreateForm, EscolaCreateForm, RatLaboratorioCreateForm, ParecerTecnicoCreateForm
from reports.serializers import ComputadorSerializer


'''
Este módulo define as seleções de dados para vizualização dos usuários.
Em geral os dados obtidos são enviados via função render(), para um template HTML, junto com o(s) objeto(s) recuperado e a requisição HTTP'''

class EscolaListView(LoginRequiredMixin, ListView):    
    login_url = '/accounts/login'
    model = Escola
    template_name = "reports/escola/list.html"
    context_object_name = 'escolas'

class EscolaDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    model = Escola
    template_name = 'reports/escola/detail.html'
    context_object_name = 'escola' 

class EscolaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Escola
    template_name = 'reports/escola/add.html'        
    form_class = EscolaCreateForm 

    def get_context_data(self, **kwargs):    
        data = super().get_context_data(**kwargs)
        if self.request.POST:            
            data["link"] = LinkDeInternetInlineForm(self.request.POST)
            data["computador"] = ComputadorInlineForm(self.request.POST)
        else:            
            data["link"] = LinkDeInternetInlineForm()
            data["computador"] = ComputadorInlineForm()
        return data
        
    def form_valid(self, form):
        context = self.get_context_data()
        
        link = context["link"]
        computador = context["computador"]
        
        self.object = form.save()
        
        if link.is_valid() and computador.is_valid():
        
            link.instance = self.object
            computador.instance = self.object
            link.save()
            computador.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        if 'save_edit' in self.request.POST:
            return reverse_lazy('reports:escola_edit', kwargs={'pk': self.object.designacao})
        elif 'save_add' in self.request.POST:
            return reverse_lazy('reports:escola_add')
        else:
            return reverse_lazy('reports:escola_list')

class EscolaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Escola
    template_name = 'reports/escola/edit.html'        
    form_class = EscolaCreateForm 
    context_object_name = 'escola'

    def get_context_data(self, **kwargs):    
        data = super().get_context_data(**kwargs)
        if self.request.POST:            
            data["link"] = LinkDeInternetInlineForm(self.request.POST)
            data["computador"] = ComputadorInlineForm(self.request.POST)
        else:            
            data["link"] = LinkDeInternetInlineForm()
            data["computador"] = ComputadorInlineForm()
        return data
        
    def form_valid(self, form):
        context = self.get_context_data()
        
        link = context["link"]
        computador = context["computador"]
        
        self.object = form.save()
        
        if link.is_valid() and computador.is_valid():
        
            link.instance = self.object
            computador.instance = self.object
            link.save()
            computador.save()
        return super().form_valid(form)       

    def get_success_url(self):
        if 'edit_del' in self.request.POST:
            return reverse_lazy('reports:escola_del', kwargs={'pk': self.object.designacao})
        elif 'edit_report' in self.request.POST:
            return reverse_lazy('reports:escola_detail', kwargs={'pk': self.object.designacao})
        elif 'save_add' in self.request.POST:
            return reverse_lazy('reports:escola_add')        
        else:
            return reverse_lazy('reports:escola_list')

class EscolaDeleteView(DeleteView):
    model = Escola
    template_name = 'reports/escola/delete.html'
    context_object_name = 'escola'
    success_url = reverse_lazy('reports:escola_list')


class RatPadraoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = RatPadrao
    template_name = 'reports/ratpadrao/add.html'        
    form_class = RatPadraoCreateForm 

    def form_valid(self, form):        
        obj = form.save(commit=False)                
        obj.tecnico = self.request.user
        obj.save()

        return super().form_valid(form)

    def get_success_url(self):
        if 'save_edit' in self.request.POST:
            return reverse_lazy('reports:rat_edit', kwargs={'pk': self.object.pk})
        elif 'save_add' in self.request.POST:
            return reverse_lazy('reports:rat_add')
        else:
            return reverse_lazy('reports:rat_list')

class RatPadraoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = RatPadrao
    template_name = 'reports/ratpadrao/edit.html'        
    form_class = RatPadraoCreateForm 
    context_object_name = 'rat'    

    def form_valid(self, form):        
        obj = form.save(commit=False)                
        obj.tecnico = self.request.user
        obj.save()

        return super().form_valid(form)

    def get_success_url(self):
        if 'edit_del' in self.request.POST:
            return reverse_lazy('reports:rat_del', kwargs={'pk': self.object.pk})
        elif 'edit_report' in self.request.POST:
            return reverse_lazy('reports:rat_detail', kwargs={'pk': self.object.pk})
        elif 'save_add' in self.request.POST:
            return reverse_lazy('reports:rat_add')        
        else:
            return reverse_lazy('reports:rat_list')

class RatPadraoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    model = RatPadrao
    template_name = 'reports/ratpadrao/detail.html'
    context_object_name = 'rat'    

class RatPadraoListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = RatPadrao
    context_object_name = 'rats'
    template_name = 'reports/ratpadrao/list.html'
    escola = None        
        
    def get_queryset(self):                
        queryset = RatPadrao.objects.all()

        escola_slug = self.kwargs.get('slug')
        if escola_slug:
            self.escola = get_object_or_404(Escola, slug=escola_slug)
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
    success_url = reverse_lazy('reports:rat_list')

class RatLaboratorioCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = RatLaboratorio
    template_name = 'reports/ratlab/add.html'        
    form_class = RatLaboratorioCreateForm 

    def get_context_data(self, **kwargs):    
        data = super().get_context_data(**kwargs)        
        if self.request.POST:            
            data["link_forms"] = LinkDeLaboratorioInlineForm(self.request.POST)            
        else:            
            data["link_forms"] = LinkDeLaboratorioInlineForm()            
        return data
        
    def form_valid(self, form):                       
                
        context = self.get_context_data()        
        link = context["link_forms"]     
        
        self.object = form.save(commit=False)
        self.object.tecnico = self.request.user        
        
        if link.is_valid():        
            link.instance = self.object            
            link.save()            
          
        return super().form_valid(form)

    def get_success_url(self):
        if 'save_edit' in self.request.POST:
            return reverse_lazy('reports:ratlab_edit', kwargs={'pk': self.object.pk})
        elif 'save_add' in self.request.POST:
            return reverse_lazy('reports:ratlab_add')
        else:
            return reverse_lazy('reports:ratlab_list')

class RatLaboratorioUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = RatLaboratorio
    template_name = 'reports/ratlab/edit.html'        
    form_class = RatLaboratorioCreateForm 
    context_object_name = 'ratlab'    

    def get_context_data(self, **kwargs):    
        data = super().get_context_data(**kwargs)
        if self.request.POST:            
            data["link_forms"] = LinkDeLaboratorioInlineForm(self.request.POST)            
        else:            
            data["link_forms"] = LinkDeLaboratorioInlineForm()            
        return data
        
    def form_valid(self, form):                       
                
        context = self.get_context_data()        
        link = context["link_forms"]     
        
        self.object = form.save(commit=False)
        self.object.tecnico = self.request.user        
        
        if link.is_valid():        
            link.instance = self.object            
            link.save()            
          
        return super().form_valid(form)

    def get_success_url(self):
        if 'edit_report' in self.request.POST:
            return reverse_lazy('reports:ratlab_detail', kwargs={'pk': self.object.pk})
        elif 'edit_add' in self.request.POST:
            return reverse_lazy('reports:ratlab_add')        
        else:
            return reverse_lazy('reports:ratlab_list')

class RatLaboratorioDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    model = RatLaboratorio
    template_name = 'reports/ratlab/detail.html'
    context_object_name = 'ratlab'    

class RatLaboratorioListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = RatLaboratorio
    context_object_name = 'ratlabs'
    template_name = 'reports/ratlab/list.html'
    escola = None        
        
    def get_queryset(self):                
        queryset = RatLaboratorio.objects.all()

        escola_slug = self.kwargs.get('slug')
        if escola_slug:
            self.escola = get_object_or_404(Escola, slug=escola_slug)
            queryset = queryset.filter(escola=self.escola)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['escola'] = self.escola
        context['escolas']= Escola.ativos.all()
        return context

class RatLaboratorioDeleteView(DeleteView):
    model = RatLaboratorio
    template_name = 'reports/ratlab/delete.html'
    context_object_name = 'rat'
    success_url = reverse_lazy('reports:ratlab_list')

class ParecerTecnicoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = ParecerTecnico
    template_name = 'reports/parecer/add.html'        
    form_class = ParecerTecnicoCreateForm 

    def get_context_data(self, **kwargs):    
        data = super().get_context_data(**kwargs)        
        if self.request.POST:            
            data["status_forms"] = StatusDeBaixaInlineForm(self.request.POST)            
        else:            
            data["status_forms"] = StatusDeBaixaInlineForm()            
        return data
        
    def form_valid(self, form):                       
                
        context = self.get_context_data()        
        link = context["status_forms"]     
        
        self.object = form.save(commit=False)
        self.object.tecnico = self.request.user        
        
        if link.is_valid():        
            link.instance = self.object            
            link.save()            
          
        return super().form_valid(form)

    def get_success_url(self):
        if 'save_edit' in self.request.POST:
            return reverse_lazy('reports:parecer_edit', kwargs={'pk': self.object.pk})
        elif 'save_add' in self.request.POST:
            return reverse_lazy('reports:parecer_add')
        else:
            return reverse_lazy('reports:parecer_list')

class ParecerTecnicoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = ParecerTecnico
    template_name = 'reports/parecer/edit.html'        
    form_class = ParecerTecnicoCreateForm 
    context_object_name = 'parecer'    

    def get_context_data(self, **kwargs):    
        data = super().get_context_data(**kwargs)
        if self.request.POST:            
            data["status_forms"] = StatusDeBaixaInlineForm(self.request.POST)            
        else:            
            data["status_forms"] = StatusDeBaixaInlineForm()            
        return data
        
    def form_valid(self, form):                       
                
        context = self.get_context_data()        
        link = context["status_forms"]     
        
        self.object = form.save(commit=False)
        self.object.tecnico = self.request.user        
        
        if link.is_valid():        
            link.instance = self.object            
            link.save()            
          
        return super().form_valid(form)

    def get_success_url(self):
        if 'edit_report' in self.request.POST:
            return reverse_lazy('reports:parecer_detail', kwargs={'pk': self.object.pk})
        elif 'edit_add' in self.request.POST:
            return reverse_lazy('reports:parecer_add')        
        else:
            return reverse_lazy('reports:parecer_list')

class ParecerTecnicoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    model = ParecerTecnico
    template_name = 'reports/parecer/detail.html'
    context_object_name = 'parecer'    

class ParecerTecnicoListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = ParecerTecnico
    context_object_name = 'pareceres'
    template_name = 'reports/parecer/list.html'
    escola = None        
        
    def get_queryset(self):                
        queryset = ParecerTecnico.objects.all()

        escola_slug = self.kwargs.get('slug')
        if escola_slug:
            self.escola = get_object_or_404(Escola, slug=escola_slug)
            queryset = queryset.filter(escola=self.escola)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['escola'] = self.escola
        context['escolas']= Escola.ativos.all()
        return context

class ParecerTecnicoDeleteView(DeleteView):
    model = ParecerTecnico
    template_name = 'reports/parecer/delete.html'
    context_object_name = 'parecer'
    success_url = reverse_lazy('reports:parecer_list')


def load_assets(request):
    escola_id = request.GET.get('escola')
    computadores = Computador.objects.filter(escola=escola_id).order_by('tipo')
    links = LinkDeInternet.objects.filter(escola=escola_id).order_by('fornecedor')
    return render(request, 'reports/ratlab/ativos_por_escola.html', {'computadores': computadores, 'links': links})

def load_computers(request):
    escola_id = request.GET.get('escola')
    computadores = Computador.objects.filter(escola=escola_id).order_by('tipo')
    return render(request, 'reports/parecer/computadores_por_escola.html', {'computadores': computadores})

class LocalDeAtendimentoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return LocalDeAtendimento.objects.none()
        qs = LocalDeAtendimento.objects.all()

        if self.q:
            qs = qs.filter(descricao__istartswith=self.q)
        
        return qs

class EscolaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Escola.objects.none()
        qs = Escola.objects.all()

        if self.q:
            qs = qs.filter(designacao__istartswith=self.q)
        
        return qs

class ComputadorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Computador.objects.none()
        qs = Computador.objects.all()

        if self.q:
            qs = qs.filter(numero_serie__istartswith=self.q)
        
        return qs

class ComputadorViewset(viewsets.ModelViewSet):
    '''Conjunto de seleções de dados para interagir com a api rest gerada pelo django-rest-framework.'''
    
    queryset = Computador.objects.all()
    serializer_class = ComputadorSerializer