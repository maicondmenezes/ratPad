from django.db.models import fields
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms

from reports.models import ParecerTecnico, RatLaboratorio, RatPadrao

class ParecerTecnicoCreateForm(forms.ModelForm):
    class Meta:
        model = ParecerTecnico
        fields = '__all__'

class RatLaboratorioCreateForm(forms.ModelForm):
    class Meta:
        model = RatLaboratorio
        fields = '__all__'

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
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()            
            self.helper.form_method = 'post'
            self.helper.form_action = '.'
            self.helper.add_input(
                Submit('submit', 'Adicionar Relatório',  css_class = 'btn btn-success btn-circle btn-lg')
            )
            self.helper.layout = Layout(
                Fieldset('', 'escola', 'locais', 'chamados'),
                Fieldset('Descrição do Problema', 'problemas', 'descricao'),
                Fieldset( 'Solução do Problema', 'solucao', 'recomendacao', 'itens_recomendados',  css_class = 'border-bottom mb-3'
                )                    
            )
        def save_model(self, request, obj, change):
            if not change:            
                obj.tecnico = request.user
                obj.save()    
        