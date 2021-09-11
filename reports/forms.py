from django import forms
from django.db.models import fields
from django.forms import inlineformset_factory, modelformset_factory

from dal import autocomplete

from reports.models import Computador, Escola, ParecerTecnico, RatLaboratorio, RatPadrao, LinkDeInternet , LinkDeLaboratorio

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

LinkDeLaboratorioInlineForm = inlineformset_factory(
    RatLaboratorio, 
    LinkDeLaboratorio, 
    fields='__all__',
    extra=3,
)

LinkDeInternetInlineForm = inlineformset_factory(
    Escola, 
    LinkDeInternet, 
    exclude=('ativo', 'data_criacao', 'dara_edicao',),
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
        fields = '__all__'
        
