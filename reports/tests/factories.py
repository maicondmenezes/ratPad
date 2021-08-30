import factory
import factory.fuzzy
from random import randint as fuzzyInt
from random import randrange
from reports.models import *
from accounts.models import User

def fakeIP():

    return f"{fuzzyInt(1, 254)}.{fuzzyInt(1, 254)}.{fuzzyInt(1, 254)}.{fuzzyInt(1, 254)}"

def fakeDesignacao():

    return f"{fuzzyInt(1, 99)}.{fuzzyInt(1, 99)}.{fuzzyInt(1, 999)}"

def fakeFone():

    return f"9 {fuzzyInt(1, 9)}{fuzzyInt(1, 9)}{fuzzyInt(1, 9)}{fuzzyInt(1, 9)} - {fuzzyInt(1, 9)}{fuzzyInt(1, 9)}{fuzzyInt(1, 9)}{fuzzyInt(1, 9)}"

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.fuzzy.FuzzyText()
    password = factory.fuzzy.FuzzyText()

    class meta:
        model = User

class EnderecoFactory(factory.django.DjangoModelFactory):    
    logradouro = factory.fuzzy.FuzzyText()
    numero = factory.fuzzy.FuzzyInteger(1,55000)
    complemento = factory.fuzzy.FuzzyText()
    bairro = factory.fuzzy.FuzzyText()
    cidade = factory.fuzzy.FuzzyText()
    uf = factory.fuzzy.FuzzyText(length=2)
    cep = factory.fuzzy.FuzzyText()
    geolocalizacao = factory.fuzzy.FuzzyText()

    class Meta:
        model = Endereco
    
class TelefoneFactory(factory.django.DjangoModelFactory):
    tipo = factory.fuzzy.FuzzyText()
    ddd = str(factory.fuzzy.FuzzyInteger(0, 99))
    operadora = str(factory.fuzzy.FuzzyInteger(0, 99))
    numero =  fakeFone()

    class Meta:
        model = Telefone
    
class LocalDeAtendimentoFactory(factory.django.DjangoModelFactory):
    descricao = factory.fuzzy

    class Meta:
        model = LocalDeAtendimento

class TipoDeProblemaFactory(factory.django.DjangoModelFactory):
    descricao = factory.fuzzy.FuzzyText()
    
    class Meta:
        model = TipoDeProblema

class TipoDeComputadorFactory(factory.django.DjangoModelFactory):
    descricao = factory.fuzzy.FuzzyText()

    class Meta:
        model = TipoDeComputador

class TipoDeLaboratorioFactory(factory.django.DjangoModelFactory):
    descricao = factory.fuzzy.FuzzyText()

    class Meta:
        model = TipoDeLaboratorio

class EscolaFactory(factory.django.DjangoModelFactory):
    designacao = fakeDesignacao()
    nome = factory.fuzzy.FuzzyText()
    endereco = factory.SubFactory(EnderecoFactory)
    telefones = factory.SubFactory(TelefoneFactory)
    email = factory.Faker("email")
    locais = [factory.SubFactory(LocalDeAtendimentoFactory)]
    ativo = factory.Faker("pybool")    
    
    class Meta:
        model = Escola

class FornecedorDeInternetFactory(factory.django.DjangoModelFactory):
    nome = factory.fuzzy.FuzzyText
    telefones = factory.SubFactory(TelefoneFactory)
    link_chamado = factory.Faker('domain_name')
    ativo= factory.Faker("pybool")    

    class Meta:
        model = FornecedorDeInternet

class LinkDeInternetFactory(factory.django.DjangoModelFactory):    
    escola = factory.SubFactory(EscolaFactory)
    fornecedor = factory.SubFactory(FornecedorDeInternet)
    velocidade = factory.fuzzy.FuzzyInteger(2, 250)
    ip_circuito = factory.Faker('ipv4')
    identificador = factory.fuzzy.FuzzyText()
    local = factory.SubFactory(LocalDeAtendimentoFactory)
    wifi = factory.Faker("pybool")
    cabo = factory.Faker("pybool")
    ativo = factory.Faker("pybool")
    funcionando = factory.Faker("pybool")   
        
    class Meta:
        model = LinkDeInternet

class RelatorioFactory(factory.django.DjangoModelFactory):
    escola = factory.SubFactory(EscolaFactory)
    locais = [factory.SubFactory(LocalDeAtendimentoFactory)]
    chamados = factory.fuzzy.FuzzyText()
    tecnico = factory.SubFactory(UserFactory)
    
    class Meta:
        model = Relatorio

class RatPadraoFactory(RelatorioFactory):
    problemas = factory.SubFactory(TipoDeProblemaFactory)
    descricao = factory.fuzzy.FuzzyText()
    solucao = factory.Faker("paragraph", nb_sentences=2, variable_nb_sentences=4)
    recomendacao = factory.Faker("pybool")
    itens_recomendados = factory.fuzzy.FuzzyText()

    class Meta:
        model = RatPadrao

class ParecerTecnicoFactory(RelatorioFactory):

    class Meta:
        model = ParecerTecnico

class ComputadorFactory(factory.django.DjangoModelFactory):
    escola = factory.SubFactory(EscolaFactory)
    local = factory.SubFactory(LocalDeAtendimentoFactory)
    tipo = factory.SubFactory(TipoDeComputadorFactory)
    marca = factory.fuzzy.FuzzyText()
    modelo = factory.fuzzy.FuzzyText()
    numero_serie = factory.fuzzy.FuzzyText()
    numero_inventario = factory.fuzzy.FuzzyText()
    sistema_operacional = factory.fuzzy.FuzzyText()
    processador = factory.fuzzy.FuzzyText()
    ram = str(factory.fuzzy.FuzzyInteger(1,8))
    hostname = factory.Faker('hostname')
    ip = factory.Faker('ipv4')
    mac_address = factory.fuzzy.FuzzyText()
    ativo = factory.Faker("pybool")
    funcionando = factory.Faker("pybool")    

    class Meta:
        model = Computador

class RatLaboratorioFactory(RelatorioFactory):
    tipo = factory.SubFactory(TipoDeLaboratorioFactory)
    fotos = factory.django.ImageField()
    links = [factory.SubFactory(LinkDeInternetFactory)]
    computadores = [factory.SubFactory(ComputadorFactory)]

    class Meta:
        model = RatLaboratorio

class StatusDeBaixaFactory(factory.django.DjangoModelFactory):
    parecer = factory.SubFactory(ParecerTecnicoFactory)
    computador = factory.SubFactory(ComputadorFactory)
    motivo = factory.fuzzy.FuzzyText()
    descricao = factory.fuzzy.FuzzyText()