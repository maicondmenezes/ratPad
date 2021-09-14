from django import forms
from django.db.models import fields
from django.forms import inlineformset_factory, modelformset_factory

from dal import autocomplete

from reports.models import Computador, Escola, ParecerTecnico, RatLaboratorio, RatPadrao, LinkDeInternet , LinkDeLaboratorio, StatusDeBaixa

class EscolaCreateForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = [
            'designacao',
            'nome',
            'endereco',
            'telefones',
            'email',
            'locais',
        ]
        widgets = {
            'locais': autocomplete.ModelSelect2Multiple(
                url='reports:local_autocomplete',
                attrs={                    
                    'data-height':100,
                    'data-minimum-input-length': 3,                    
                },
            ),
        }

class RatPadraoCreateForm(forms.ModelForm):           
    class Meta:
        model = RatPadrao
        fields = [
            'escola',
            'locais',
            'chamados',
            'problemas',
            'descricao',
            'solucao',
            'recomendacao',
            'itens_recomendados'
        ]                       
        widgets = {
            'escola': autocomplete.ModelSelect2(
                url='reports:escola_autocomplete',
                attrs={                    
                    'data-height':140,
                    'data-minimum-input-length': 4,                    
                },
            ),            
        }

class RatLaboratorioCreateForm(forms.ModelForm):   
    class Meta:
        model = RatLaboratorio
        fields = [
            'escola',
            'locais',
            'chamados',
            'tipo',
            'fotos',            
            'computadores',
        ]                       
        widgets = {
            'escola': autocomplete.ModelSelect2(
                url='reports:escola_autocomplete',
                attrs={                    
                    'data-height':140,
                    'data-minimum-input-length': 4,                    
                },
            ),
            'locais': autocomplete.ModelSelect2Multiple(
                url='reports:local_autocomplete',
                attrs={                    
                    'data-height':100,
                    'data-minimum-input-length': 3,
                    'data-maximum-selection-length': 1
                },
            ),            
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['computadores'].queryset = Computador.objects.none()

        if 'escola' in self.data:
            try:
                escola_id = str(self.data.get('escola'))
                self.fields['computadores'].queryset = Computador.objects.filter(escola=escola_id).order_by('tipo')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['computadores'].queryset = self.instance.escola.computador_set.order_by('tipo')

class LinkDeLaboratorioForm(forms.ModelForm):
    class Meta:
        model = LinkDeLaboratorio
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].queryset = LinkDeInternet.objects.none()

        if 'link' in self.data:
            try:
                link_id =int(self.data.get('link'))
                link = LinkDeInternet.objects.get(id=link_id)                
                self.fields['link'].queryset = LinkDeInternet.objects.filter(escola=link.escola).order_by('fornecedor')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['link'].queryset = self.instance.escola.linkdeinternet_set.all()

class StatusDeBaixaForm(forms.ModelForm):
    class Meta:
        model = StatusDeBaixa
        fields=['computador', 'motivo', 'descricao']

    widgets = {
            'computador': autocomplete.ModelSelect2(
                url='reports:computador_autocomplete',
                attrs={                    
                    'data-height':140,
                    'data-minimum-input-length': 4,                    
                },
            ),            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['computador'].queryset = Computador.objects.none()

        if 'computador' in self.data:
            try:
                computador_id =int(self.data.get('computador'))
                computador = Computador.objects.get(id=computador_id)                
                self.fields['computador'].queryset = Computador.objects.filter(escola=computador.escola.designacao).order_by('tipo')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['computador'].queryset = self.instance.escola.computador_set.all()


LinkDeLaboratorioInlineForm = inlineformset_factory(
    RatLaboratorio, 
    LinkDeLaboratorio, 
    form=LinkDeLaboratorioForm,
    fields='__all__',
    extra=3,
)

StatusDeBaixaInlineForm = inlineformset_factory(
    ParecerTecnico, 
    StatusDeBaixa, 
    form=StatusDeBaixaForm,
    fields='__all__',
    extra=6,
)

LinkDeInternetInlineForm = inlineformset_factory(
    Escola, 
    LinkDeInternet, 
    fields='__all__',
    extra=3,
)

ComputadorInlineForm = inlineformset_factory(
    Escola, 
    Computador, 
    exclude=('escola', 'ativo', 'data_criacao', 'dara_edicao'),
    extra=5,
)

class ParecerTecnicoCreateForm(forms.ModelForm):
    class Meta:
        model = ParecerTecnico
        fields = [
            'escola',
            'locais',
            'chamados',                            
        ]                       
        widgets = {
            'escola': autocomplete.ModelSelect2(
                url='reports:escola_autocomplete',
                attrs={                    
                    'data-height':140,
                    'data-minimum-input-length': 4,                    
                },
            ),
            'locais': autocomplete.ModelSelect2Multiple(
                url='reports:local_autocomplete',
                attrs={                    
                    'data-height':100,
                    'data-minimum-input-length': 3,
                    'data-maximum-selection-length': 1
                },
            ),
        }