from django import forms
from django.forms import widgets

from dal import autocomplete

from reports.models import Escola, ParecerTecnico, RatLaboratorio, RatPadrao

class ParecerTecnicoCreateForm(forms.ModelForm):
    class Meta:
        model = ParecerTecnico
        fields = '__all__'

class RatLaboratorioCreateForm(forms.ModelForm):
    class Meta:
        model = RatLaboratorio
        fields = '__all__'

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