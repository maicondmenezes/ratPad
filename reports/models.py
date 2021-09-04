from datetime import timedelta
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib import admin
from accounts.models import User

from . import choices
''' Este módulo define as regras de negócio do sistema.
    
    Cada classe modela uma entidade e suas relações.
    As regras de validação dos dados e estrutura do banco de dados relacional também são definidas a partir destas classes
'''
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ativo=True)

class CreatorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tecnico=self.tecnico)

class Endereco(models.Model):
    '''
    Enderço das escolas e usuários cadastrados no sistema
    '''
    logradouro = models.CharField(max_length=120, blank=True)
    numero = models.IntegerField(blank=True)
    complemento = models.CharField(max_length=120, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    uf = models.CharField(max_length=2, choices=choices.UF, blank=True)
    cep = models.CharField(max_length=12, blank=True)
    geolocalizacao = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return (f'{self.logradouro}, {self.numero}, {self.complemento}\n'
        f'CEP.: {self.cep}\n'
        f'{self.bairro} - {self.cidade} - {self.uf} - Brasil\n')

class Telefone(models.Model):
    tipo = models.CharField(max_length=20, choices=choices.TIPOS_DE_TELEFONE)
    ddd = models.CharField(max_length=2)
    operadora = models.CharField(max_length=20, choices=choices.OPERADORAS_DE_TELEFONIA)
    numero =  models.CharField(max_length=15)

    def __str__(self):
        return f'{self.tipo}: ({self.ddd}) {self.numero} - {self.operadora}'

class LocalDeAtendimento(models.Model):
    '''
    As salas que possuem ativos de informática dentro de uma unidade escolar.
    Cada Escola possui um subconjunto de locais de atendimento, derivado de referências as instâncias desse modelo.
    Cada Relatório possui um subconjunto derivado de referências as instâncias deste modelo referenciadas na escola atendida.
    Cada Computador possui uma referência a uma única instância deste modelo referenciada na Escola onde ele está relacionado.
    Cada Link De Internet possui uma referência a uma única instâncida deste modelo referenciada na Escola onde ele está relacionado.
    
    Args:
        descricao (str): O nome identificado na porta da sala

    Attributes:
        descricao (str): O nome identificado na porta da sala
    '''
    
    descricao = models.CharField(max_length=100)

    def __str__(self):
        '''Define o atributo descrição como representação textual de uma instância do modelo.'''
        return self.descricao

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Local de Atendimento'
        verbose_name_plural = 'Locais de Atendimento'

class TipoDeProblema(models.Model):
    '''
    Os tipos de problemas solucionados em um atendimento técnico
    Cada Relatório de Atendimento Técnico possui um subconjunto derivado de instâncias deste modelo.
        
    Args:
        descricao (str): A especificação de um problema técnico em uma única palavra (ex:. Hardwarem, Software)

    Attributes:
        descricao (str): A especificação de um problema técnico.
    '''

    descricao = models.CharField(max_length=20)

    def __str__(self):
        '''Define o atributo descrição como representação textual de uma instância do modelo.'''
        return self.descricao

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Tipo de Problema'
        verbose_name_plural = 'Tipos de Problema'

class TipoDeComputador(models.Model):
    '''
    Os tipos de Computadores encontrados nas Escolas atendidas
    Cada Computador possui uma única instância deste modelo.
        
    Args:
        descricao (str): A especificação de um tipo de computador pessoal em uma única palavra (ex:. Desktop, Notebook)

    Attributes:
        descricao (str): A especificação de um tipo de computador pessoal.
    ''' 
    descricao = models.CharField(max_length=50)

    def __str__(self):
        '''Define o atributo descrição como representação textual de uma instância do modelo.'''
        return self.descricao

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Tipo de Computador'
        verbose_name_plural = 'Tipos de Computador'

class TipoDeLaboratorio(models.Model):
    '''
    Os tipos de Laboratórios encontrados nas Escolas atendidas
    Cada Relatório de Atendimento de Laboratório possui um subconjunto derivado de referências as instâncias desse modelo.
        
    Args:
        descricao (str): A especificação de um tipo de laboratório em uma única palavra (ex:. Comum, Proinfo Rural)

    Attributes:
        descricao (str): A especificação de um tipo de laboratório.
    ''' 
    descricao = models.CharField(max_length=20)

    def __str__(self):
        '''Define o atributo descrição como representação textual de uma instância do modelo.'''
        return self.descricao

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Tipo de Laboratório'
        verbose_name_plural = 'Tipos de Laboratório'

class Escola(models.Model):
    '''
    As escolas da rede atendidas em cada relatório
    Cada Computador possui uma referência a uma única instância desse modelo.
    Cada Link de Internet possui uma referência a uma única instância desse modelo.
    Cada Relatório possui uma referência a uma única instância desse modelo.
        
    Args:
        designacao (str): Código de identificação de uma unidade escolar no formato CC.RR.UUU (CC= Coordenadoria; RR= Região; UUU= Unidade escolar) 
        nome (str): Nome por extenso da unidade escolar iniciado pelo tipo da unidade (Ex.: Escola Municipal, Creche Municipal, etc.)
        endereco (str): logradouro número e outros complementos de identificação do endereço
        bairro (str): Bairro e Subbairro da unidade escolar
        cep (str): CEP da unidade escolar
        telefones (str): telefones da unidade escolar 
        email (str): email da unidade escolar
        locais (fk): lista de chaves estrangeiras referenciando as salas com aitvos de informática na unidade escolar        
        ativo(bool): identifica se a unidade escolar existe e está em funcionamento
        data_criacao(data): data de inclusão no sistema
        data_edicao (data): data da última modificação

    Attributes:
        designacao (str): Código de identificação de uma unidade escolar.
        nome (str): Nome por extenso da unidade escolar.
        endereco (str): logradouro número e outros complementos.
        bairro (str): Bairro e Subbairro da unidade escolar.
        cep (str): CEP da unidade escolar.
        telefones (str): telefones da unidade escolar.
        email (email): email da unidade escolar.
        locais (fk): lista de chaves estrangeiras referenciando as salas com aitvos de informática na unidade escolar.
        ativo(bool): identifica se a unidade escolar existe e está em funcionamento
        data_criacao(data): data de inclusão no sistema
        data_edicao (data): data da última modificação
    ''' 
    designacao = models.CharField(max_length=10, primary_key=True, unique=True)    
    nome = models.CharField(max_length=200)    
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)    
    telefones = models.ManyToManyField(Telefone, blank=True)
    email = models.EmailField(blank=True)
    locais = models.ManyToManyField(LocalDeAtendimento, blank=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_edicao  = models.DateTimeField(auto_now_add=True, null=True)
    
    objects = models.Manager()
    ativos = ActiveManager()

    def __str__(self):
        '''Define o atributo desginação seguido do nome da unidade escolar como representação textual de uma instância do modelo.'''
        return f'({self.designacao}) {self.nome}'
    
    def get_absolute_url(self):
        return reverse('reports:report_escola', kwargs={'designacao': self.designacao})

class FornecedorDeInternet(models.Model):
    '''
    As operadoras e/ou contratos específicos de prestação de serviço de internet para as unidades escoilares
    Cada Link De Internet possui uma referência a uma única instância desse modelo.
        
    Args:
        nome(str): Nome fantasia da empresa fornecedora ou nome utilizado para identificar um contrato específco para a SME (Ex.: OI-MEC)
        telefone(str): Teledone para solicitação de assistência técnica.
        link_chamado(url): url para solicitação de assistência técnica.
        ativo(bool): identifica se o fornecedor existe e ainda atende a SME.
        data_criacao(data): data de inclusão no sistema.
        data_edicao (data): data da última modificação.

    Attributes:
        nome(str): Nome fantasia da empresa fornecedora ou nome utilizado para identificar um contrato específco para a SME (Ex.: OI-MEC)
        telefone(str): Teledone para solicitação de assistência técnica.
        link_chamado(url): url para solicitação de assistência técnica.
        ativo(bool): identifica se o fornecedor existe e ainda atende a SME.
        data_criacao(data): data de inclusão no sistema.
        data_edicao (data): data da última modificação.
    ''' 
    nome = models.CharField(max_length=20)
    telefones = models.ManyToManyField(Telefone, blank=True)
    link_chamado = models.URLField()
    ativo= models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_edicao  = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()
    ativos = ActiveManager()

    def __str__(self):
        '''Define o atributo nome como a representação textual de uma instância do modelo.'''
        return self.nome

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Fornecedor de Internet'
        verbose_name_plural = 'Fornecedores de Internet'

class LinkDeInternet(models.Model):
    '''
    Os links de internet instalados em uma unidade escolar
    Cada Escola possui um subconjunto de referências derivado das instâncias desse modelo.
        
    Args:
        escola (fk): Chave estrangeira identificando a escola que o link está instalado (designação da escola)
        fornecedor (fk): Chave estrangeira identificando o fornecedor que disponibiliza o serviço
        velocidade (int): velocidade de conexão em Mbps (Megabits por segundo) contratada pela unidade escolar
        ip_circuito (ip): endereço IP do serviço.
        identificador (str): código identificador do link junto ao fornecedor.        
        local(fk): Chave estrangeira identificando o local onde o link foi instalado
        wifi (bool): identifica se a conexão está disponível via infraestrutura sem fio.
        cabo (bool): identifica se a conexão está disponível via infraestrutura cabeada.
        ativo(bool): identifica se o link existe e está ativo.
        funcionando(bool): identifica se o link está em funcionamento ou não
        data_criacao(data): data de inclusão no sistema.
        data_edicao (data): data da última modificação.

    Attributes:
        escola (fk): designação da escola que o link está instalado
        fornecedor (fk): Identificador do fornecedor que disponibiliza o serviço
        velocidade (int): velocidade de conexão.
        ip_circuito (ip): endereço IP do serviço.
        identificador (str): código identificador do link junto ao fornecedor.
        local(fk): Chave estrangeira identificando o local onde o link foi instalado.
        wifi (bool): identifica se a conexão está disponível via infraestrutura sem fio.
        cabo (bool): identifica se a conexão está disponível via infraestrutura cabeada.
        ativo(bool): identifica se o link existe e está ativo.
        funcionando(bool): identifica se o link está em funcionamento ou não
        data_criacao(data): data de inclusão no sistema.
        data_edicao (data): data da última modificação.
    ''' 
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True)
    fornecedor = models.ForeignKey(FornecedorDeInternet, on_delete=models.CASCADE)
    velocidade = models.IntegerField()
    ip_circuito = models.GenericIPAddressField()
    identificador = models.CharField(max_length=20)
    local = models.ForeignKey(LocalDeAtendimento, on_delete=models.CASCADE, null=True)
    wifi = models.BooleanField(default=True)
    cabo = models.BooleanField(default=True)
    ativo = models.BooleanField(default=True)
    funcionando = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_edicao  = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()
    ativos = ActiveManager()

    def __str__(self):
        '''Define o atributo fornecedor seguido por velocidade, identificador e escola, como  representação textual de uma instância do modelo.'''
        return f'{self.fornecedor} - {self.velocidade} Mbps - {self.identificador} - {self.escola}'

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Link de Internet'
        verbose_name_plural = 'Links de Internet'

class Relatorio(models.Model):
    '''
    O modelo geral para todos relatórios gerados no sistema
    Cada tipo específico de relatório referencia uma única instância deste modelo
        
    Args:
        escola (fk): Chave estrangeira identificando a escola que o atendimento foi realizado
        locais (fk): lista de chaves estrangeiras identificando as salas da unidade escolar atendidas
        chamados (str): lista de identificadores dos chamados atendidos
        tecnico (fk): chave estrangeira identificano o técnico que gerou o relatório. Gerada automaticamente
        data_criacao(data): data de inclusão no sistema. Gerada automaitcamento
        data_edicao (data): data da última modificação. Gerada automaticamente

    Attributes:
        escola (fk): Chave estrangeira identificando a escola que o atendimento foi realizado
        locais (fk): lista de chaves estrangeiras identificando as salas da unidade escolar atendidas
        chamados (str): lista de identificadores dos chamados atendidos
        tecnico (fk): chave estrangeira identificano o técnico que gerou o relatório. Gerada automaticamente
        data_criacao(data): data de inclusão no sistema. Gerada automaitcamento
        data_edicao (data): data da última modificação. Gerada automaticamente
    ''' 
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    locais = models.ManyToManyField(LocalDeAtendimento)
    chamados = models.CharField(max_length=200)
    tecnico = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_edicao  = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()
    criados_por_este_tecnico = CreatorManager()
    
    ''' Configuração da exibição da lista de relatórios no módulo administrativo do django, ordenando por data mais recente'''
    @admin.display(boolean=True, ordering='data', description='Atendimento Recente?',)

    def __str__(self):
        '''Define o atributo escola seguido pela data em formato 'dd-mm-aaaa H:M' como representação textual de uma instância do modelo.'''
        return f'''{self.escola} - {self.data_criacao.strftime('%d-%m-%Y %H:%M')}'''

    def recente(self):
        ''' Retorna True se o relatório foi gerado no máximo no dia anterior'''
        return self.data_criacao >= timezone.now() - timedelta(days=1)
       
    class meta:
        ''' Define o modelo como uma classe abstrata que não pode ser instânciada'''
        abstract = True

class RatPadrao(Relatorio):
    '''
    O Relatório de Atendimento Técnico padrão gerado em todas as visitas as unidades escolares.
    Estende o relatório padrão    
        
    Args:
        problemas (fk): lista de chaves estrangeiras identificando os problemas solucionados.
        descricao (str): descrição curta do problema relatado pelo solicitante
        solucao (str): texto descritivo resumindo as ações tomadas pelo técnico nmo atendimento.
        recomendacao (bool): identifica se houve alguma recomendação de aquisição ou compra de novos equipamentos e/ou serviços
        itens_recomendados (str): lista de equipamentos e/ou serviços recomendados pelo técnico

    Attributes:
        problemas (fk): lista de chaves estrangeiras identificando os problemas solucionados.
        descricao (str): descrição curta do problema relatado pelo solicitante
        solucao (str): texto descritivo resumi'status',ndo as ações tomadas pelo técnico nmo atendimento.
        recomendacao (bool): identifica se houve alguma recomendação de aquisição ou compra de novos equipamentos e/ou serviços
        itens_recomendados (str): lista de equipamentos e/ou serviços recomendados pelo técnico        
    ''' 
    problemas = models.ManyToManyField(TipoDeProblema)
    descricao = models.CharField(max_length=200)
    solucao = models.TextField(max_length=1000)
    recomendacao = models.BooleanField(default=False)
    itens_recomendados = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Relatório de Atendimento Técnico'
        verbose_name_plural = 'Relatórios de Atendimento Técnico'

    def __str__(self):
        '''Define o atributo descrição como representação textual de uma instância do modelo.'''
        return self.descricao
    
    def get_absolute_url(self):
        return reverse('reports:rat_detail', kwargs={'pk': self.id})

class ParecerTecnico(Relatorio):
    '''
    O Relatório de Parecer Técnico para baixa e descarte de equipamentos que não puderam ser recuperados em um atendimento, estende o relatório padrão.
    Cada Status De Baixa está relacionado a uma única instância deste modelo.
    '''            
    
    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Parecer Técnico'
        verbose_name_plural = 'Relatórios de Parecer Técnico'
    
    def get_absolute_url(self):
        return reverse('reports:report_parecer', kwargs={'id': self.id})

class Computador(models.Model):
    '''
    Computadores atendidos nas unidades escolares da SME.    
    Cada Relatório de Atendimento de Laboratŕoio referencia um subconjunto derivado de instâncias deste modelo.
    Cada Parecer Técnico de Baixa referencia um subconjunto derivado de instâncias deste modelo.
        
    Args:
        escola (fk): Chave estrangeira identificando a escola que o computador esta relacionado.
        local(fk): Chave estrangeira identificando o local na Escola onde o computador está instalado
        tipo (fk): Chave estrangeira identificando o tipo do Computador. (Ex.: Notebook)
        marca (str): Marca do fabricante do computador
        modelo (str): Modelo Específico do computador
        numero_serie (str): Número de série de identificação única do computador
        numero_inventario (str): Código de inventário relacionando o computador a unidade escolar
        sistema_operacional (str): Sistema operacional instalado no computador (obtido automaticamente pelo ratPad Asset Manager)
        processador (str): Identificação do fabricante e modelo do processador do computador (obtido automaticamente pelo ratPad Asset Manager)
        ram (int): quantidade de memória ram em Gigabytes disponível no computador (obtido automaticamente pelo ratPad Asset Manager)
        hostname (str): nome que identifica o computador na rede. a regra de nomeção é ECCRRUUU-XXX (onde CCRRUUU é a designação da escola e XXX o número identificador no computador)
        ip (ip): endereço de rede do computador
        mac_address (str): endereço mac único do computador
        ativo(bool): identifica se o computador existe e está ativo.
        funcionando(bool): identifica se o computador está em funcionamento ou não
        data_criacao(data): data de inclusão no sistema.
        data_edicao (data): data da última modificação.

    Attributes:
        escola (fk): Chave estrangeira identificando a escola que o computador esta relacionado.
        local(fk): Chave estrangeira identificando o local na Escola onde o computador está instalado
        tipo (fk): Chave estrangeira identificando o tipo do Computador. (Ex.: Notebook)
        marca (str): Marca do fabricante do computador
        modelo (str): Modelo Específico do computador
        numero_serie (str): Número de série de identificação única do computador
        numero_inventario (str): Código de inventário relacionando o computador a unidade escolar
        sistema_operacional (str): Sistema operacional instalado no computador (obtido automaticamente pelo ratPad Asset Manager)
        processador (str): Identificação do fabricante e modelo do processador do computador (obtido automaticamente pelo ratPad Asset Manager)
        ram (int): quantidade de memória ram em Gigabytes disponível no computador (obtido automaticamente pelo ratPad Asset Manager)
        hostname (str): nome que identifica o computador na rede. a regra de nomeção é ECCRRUUU-XXX (onde CCRRUUU é a designação da escola e XXX o número identificador no computador)
        ip (ip): endereço de rede do computador
        mac_address (str): endereço mac único do computador
        ativo(bool): identifica se o computador existe e está ativo.
        funcionando(bool): identifica se o computador está em funcionamento ou não
        data_criacao(data): data de inclusão no sistema.
        data_edicao (data): data da última modificação.
    ''' 
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True)
    local = models.ForeignKey(LocalDeAtendimento, on_delete=models.CASCADE, null=True)
    tipo = models.ForeignKey(TipoDeComputador, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=20, unique=True, primary_key=True)
    numero_inventario = models.CharField(max_length=20, unique=True)
    sistema_operacional = models.CharField(max_length=20)    
    processador = models.CharField(max_length=100)
    ram = models.CharField(max_length=20)
    hostname = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    funcionando = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_edicao  = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()
    ativos = ActiveManager()

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Computador'
        verbose_name_plural = 'Computadores'

    def __str__(self):
        '''Define o atributo número de série seguido de inventario, tipo, marca e modelo como representação textual de uma instância do modelo.'''
        return f'{self.numero_serie} - {self.numero_inventario} - {self.tipo} - {self.marca} - {self.modelo}'

class RatLaboratorio(Relatorio):
    '''
    O Relatório de Atendimento de Laboratório gerado em caso de verificação técnica ao laboratório da unidade escolar.
    Estende o relatório padrão    
        
    Args:
        tipo (fk): Chave estrangeira que identidica o tipo de laboratório atendido no relatório.
        fotos (img): fotos identificando a situação geral do laboratório após o atendimento.
        computadores (fk): lista de chaves estrangeiras identificando os computadores presentes no laboratório
        links (fk): lista de chaves estrangeiras identificando os links de internet  presentes no laboratório.

    Attributes:
        tipo (fk): Chave estrangeira que identidica o tipo de laboratório atendido no relatório.
        fotos (img): fotos identificando a situação geral do laboratório após o atendimento.
        computadores (fk): lista de chaves estrangeiras identificando os computadores presentes no laboratório
        links (fk): lista de chaves estrangeiras identificando os links de internet  presentes no laboratório.
    ''' 
    tipo = models.ForeignKey(TipoDeLaboratorio, on_delete=models.CASCADE, default='1')
    fotos = models.ImageField(upload_to='fotosLab', blank=True)    
    links = models.ManyToManyField(LinkDeInternet)
    computadores = models.ManyToManyField(Computador)

    class Meta:
        '''Define a representação textual do modelo na forma singular e plural no modúlo administrativo do django'''
        verbose_name = 'Relatório de Laboratório'
        verbose_name_plural = 'Relatórios de Laboratório'

    def get_absolute_url(self):
        return reverse('reports:report_lab', kwargs={'id': self.id})

class StatusDeBaixa(models.Model):
    '''
    O Motivo detalhado da situação de baixa de cada computador relacionado em um Parecer Técnico de Baixa    
        
    Args:
        parecer (fk): Chave estrangeira identificando o Parecer Técnico de Baixa que o Status está relacionado
        computador (fk): Chave estrangeira que identifica Computador que será descartado
        motivo (fk): Chave estrangeira que identifica o motivo da baixa do Computador
        descricao (str): descrição por extenso do motivo pelo qual o computador será descartado.

    Attributes:
        parecer (fk): Chave estrangeira identificando o Parecer Técnico de Baixa que o Status está relacionado
        computador (fk): Chave estrangeira que identifica Computador que será descartado
        motivo (fk): Chave estrangeira que identifica o motivo da baixa do Computador
        descricao (str): descrição por extenso do motivo pelo qual o computador será descartado.
    ''' 
    parecer = models.ForeignKey(ParecerTecnico, on_delete=models.CASCADE, null=True)
    computador = models.OneToOneField(Computador, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=20, choices=choices.MOTIVOS_DE_BAIXA, default='Imprestabilidade')
    descricao = models.CharField(max_length=200)

    def __str__(self):
        '''Define o atributo equipamento seguido do motivo e descrição do motivo como representação textual de uma instância do modelo.'''
        return f'{self.computador} - {self.motivo} - {self.descricao}'