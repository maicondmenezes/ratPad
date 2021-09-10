from django import forms
from django.db.models import fields
from django.forms import inlineformset_factory, modelformset_factory

from dal import autocomplete

from reports.models import Computador, Endereco, Escola, ParecerTecnico, RatLaboratorio, RatPadrao, Telefone, FornecedorDeInternet, LinkDeInternet 

TelefoneInlineForm = modelformset_factory(
    Telefone, 
    exclude=('ativo', 'data_criacao', 'dara_edicao',),
    extra=3,
)

LinkDeInternetInlineForm = inlineformset_factory(
    Escola, 
    LinkDeInternet, 
    fields=(
        'fornecedor',
        'velocidade',
        'ip_circuito',
        'identificador',
        'local',
        'wifi',
        'cabo',
        'funcionando',),
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