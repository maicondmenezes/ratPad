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