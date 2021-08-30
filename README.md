# ratPad admin 0.1.4.5b
_Gerenciador de relatórios de atendimentos técnicos da 10ª CRE - RJ_

Updates:
- _0.1.4.5b_ = front-end aplicado, a partir deste ponto o projeto se divide entre ratPad admin e ratPad para usuários 
- _0.1.3.6b_ = implementar tecman para planilha de custos de deslocamento e gestão de rotas
- _0.1.3.5b_ = cadastro automatizado de computadores via app local
- _0.1.3.4b_ = versão estavél dos 3 relatórios principais (RAT Padrão, PArecer Técnico de Baixas e RAT de Laboratórios); cadastro de não automatizado de computadores; sistema _ainda não possui tratamento de erros_

## TO DO:
- [ ] Normalizar informações de endereço e telefones da Escola
- [ ] Incluir daods de geo localização no endereço das escolas
- [ ] Consumir API do Google Maps para localização dos endereços e rotas de onibus das escolas
- [ ] Consultar API's de CIA's de transporte urbano para mensurar tempo de espera de linhas.
- [ ] Criar uma tela boas vindas do sistema com atalho para os relatórios e para area de gestão do tecnico _(tecman será o novo app)_
- [X] Iniciar a documentação do projeto
    - [ ] Detalhar o propósito do sistema no arquivo readme
    - [ ] Traduzir o documento para o inglês
    - [X] fazer o pydoc de cada modulo
- [X] criar TESTES
- [ ] criar user para os tecnicos e supervisores
- [ ] exibir os relatórios apenas do usuário criador
- [ ] criar rodape do sistema com minha informaçṍes
- [ ] criar botão de import
- [ ] criar botão de export
- [X] Criar API rest para envio de infomações dos computadores apenas
- [X] Criar app local de captura automatizada dos informações dos computadores
- [X] tentar instalar grappelli no pythonanywhere 
- [X] popular a base com as escolas
- [X] popular a base com as RAT's
- [X] popular a base com tabelas fixas novas (local, tipos, etc.)
- [X] criar formularios administrativos para os relatorios novos
- [X] criar template de relatórios de parecer e laboratório para impressão
    - [X] criar estrutura de tabelas para a lista de computadores da rat  de laboratorio
    - [X] modificar a estrutura de relacionamento entre links de internet e escolas
    - [X] _resolver bug de local de antedimento do template de rat de laboratorio_
- [X] migrar a base existente para o novo padrao (adaptar as novas tabelas de tipos)
    - [X] Popular a base nova (Escolas, RATS, Fornecedores e Links de Internet) _falta fornecedores, links e o restante das escolas com endereço_
    - [X] Desenvolver função de captura das informações de um computador
- [X] encapsular o sistema em uma sessão de usuário
- [x] migrar a base para um SGDB mais robusto (postgree)
- [x] pesquisar um template bom no startbootstrap.com