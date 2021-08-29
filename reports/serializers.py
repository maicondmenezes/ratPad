from rest_framework import serializers

from reports.models import *

'''Este módulo define a automação da serialização de objetos do banco de dados para envio via API do plugin django-rest-framework.'''


class EnderecoSerializer(serializers.ModelSerializer):
    '''Serializador dos Endreços das escolas cadastradas no sistema'''
    class Meta:
        model = Endereco
        fields = '__all__'

class LocalDeAtendimentoSerializer(serializers.ModelSerializer):
    '''Serializador dos Locais De Atendimento cadastrados no sistema'''
    class Meta:
        model = LocalDeAtendimento
        fields = '__all__'

class TipoDeProblemaSerializer(serializers.ModelSerializer):
    '''Serializador dos Tipos De Problema cadastrados no sistema'''
    class Meta:
        model = TipoDeProblema
        fields = '__all__'

class TipoDeComputadorSerializer(serializers.ModelSerializer):
    '''Serializador dos Tipos De Computador cadastrados no sistema'''
    class Meta:
        model = TipoDeComputador
        fields = '__all__'

class TipoDeLaboratorioSerializer(serializers.ModelSerializer):
    '''Serializador dos Tipos De Laboratório no sistema'''
    class Meta:
        model = TipoDeLaboratorio
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    '''Serializador das Enderecos cadastradas no sistema'''
    class Meta:
        model = Endereco
        fields = '__all__'

class EscolaSerializer(serializers.ModelSerializer):
    '''Serializador das Escolas cadastradas no sistema'''
    class Meta:
        model = Escola
        fields = '__all__'

class FornecedorDeInternetSerializer(serializers.ModelSerializer):
    '''Serializador dos Fornecedores De Internet cadastrados no sistema'''
    class Meta:
        model = FornecedorDeInternet
        fields = '__all__'

class LinkDeInternetSerializer(serializers.ModelSerializer):
    '''Serializador dos Links De Internet cadastrados no sistema'''
    class Meta:
        model = LinkDeInternet
        fields = '__all__'

class RelatorioSerializer(serializers.ModelSerializer):
    '''Serializador dos computadores cadastrados no sistema'''
    class Meta:
        model = Relatorio
        fields = '__all__'

class RatPadraoSerializer(RelatorioSerializer):
    '''Serializador dos Relatório de Atendimento Técnico cadastrados no sistema'''
    class Meta:
        model = RatPadrao
        fields = '__all__'

class ParecerTecnicoSerializer(RelatorioSerializer):
    '''Serializador dos Pareceres Técnicos de Baixa cadastrados no sistema'''
    class Meta:
        model = ParecerTecnico
        fields = '__all__'

class RatLaboratorioSerializer(RelatorioSerializer):
    '''Serializador dos Relatórios de Atendimento de Laboratórios cadastrados no sistema'''
    class Meta:
        model = RatLaboratorio
        fields = '__all__'

class StatusDeBaixaSerializer(serializers.ModelSerializer):
    '''Serializador dos Status De Baixa cadastrados no sistema'''
    class Meta:
        model = StatusDeBaixa
        fields = '__all__'

class ComputadorSerializer(serializers.ModelSerializer):
    '''Serializador dos computadores cadastrados no sistema'''
    class Meta:
        model = Computador
        fields = '__all__'
