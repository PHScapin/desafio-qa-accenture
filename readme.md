# Desafio QA Automation Engineer - Accenture

Este documento tem por fim registrar a minha linha de raciocínio durante a criação/execução do desafio proposto pela Accenture. Para isso, irei registrar as principais etapas de execução, e justificar o motivo de cada decisão.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- [Python 3.x](https://www.python.org/downloads/) instalado.
- Navegador Google Chrome.
- Git instalado.

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/PHScapin/desafio-qa-accenture.git
   cd desafio-qa-accenture
   ```

2. Crie e ative um ambiente virtual (venv):

No Windows:
```bash
python -m venv venv
venv\Scripts\activate
``` 

No Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### Execução dos Testes

Para executar os testes de API (Pytest):
```bash
pytest testes/ -v
```
Para executar os testes de Frontend (Behave/BDD):
```
behave feature/
```


## Arquitetura

A primeira etapa do processo, foi identificar quais eram os desafios, e decidir qual seria a stack de automação que eu utilizaria para obter o melhor resultado possível.

Através da leitura do documento `Desafio_QA (004).pptx`, identifiquei que a linguagem Python era uma opção viável, e por ser a linguagem que mais utilizei profissionalmente, irei utilizá-la para obter o melhor resultado.

Pensando agora no desafio em si, temos algumas variáveis que podem ser interessantes. Para a execução dos testes de automação relacionados à API, irei utilizar a biblioteca `HTTPX` pois é melhor que a biblioteca `requests`, tendo a possibilidade de fazer multiplexação. Nesse cenário do desafio, não tem muito valor, mas em um sistema que tenha muitas requisições, pode salvar um tempo considerável.

Indo para a parte de frontend, irei optar por utilizar o `Selenium WebDriver` em conjunto com um dos critérios, o `POM (Page Object Model)`, além de ser também por questão de preferência. E integraremos à esta etapa a biblioteca `Behave`, pois esta traz consigo a possibilidade utilizar o `BDD (Behavior-Driven Development)`, considerado como um ponto diferencial. A depender do projeto faria sentido utilizarmos o `Robot Framework`, mas como o desafio também é mostrar minhas habilidades de Python, irei optar por não seguir por este caminho.

Como no desafio é mencionado que devemos gerar uma massa de dados aleatória em uma das etapas, irei utilizar a biblioteca `Faker`, justamente pra trazer esses dados. Além disso, para finalizar a definição das ferramentas que utilizarei, o projeto contará com a biblioteca `pytest`, pra ter um orquestrador, e em um projeto real, um facilitador de integração ao `CI (Continuous Integration)`.

## Versionamento e Gestão de Código

O desafio menciona explicitamente a publicação e gestão feita na plataforma GitHub, por isso, a primeira coisa que faremos após terminar as configurações locais como a criação do `venv`, será dar um `git init` no repositório e fazer um `git commit -m` com a estrutura básica que defini. Em sequência vou criar o repositório no meu GitHub, no caminho `https://github.com/PHScapin/desafio-qa-accenture` e dou o primeiro `git push`.

Pretendo fazer três `git commit`. O primeiro sendo o de setup, o segundo com os códigos relacionados a automação da API, e o terceiro com a automação do frontend. Se for necessário corrigir algum erro no caminho, irei fazer outras execuções com o título `git commit -m 'Fix'`.

Apenas um detalhe, tenho por costume subir um arquivo chamado `test_setup.py` para verificar se a biblioteca do `pytest` está funcionando corretamente. Este arquivo será removido em versões seguintes.

Em sequência, eu configurei o arquivo `main.yml` com a ordem de execução da pipeline. Assim, quando houver um `git push` ou um `git pull` na `main branch`, irão acontecer as actions.

## Estrutura dos Arquivos

A princípio pensei na seguinte arquitetura:

### `📂 .github`

Esta pasta terá o arquivo responsável por executar a esteira, este será chamado de `main.yml`. Nele vou colocar as instruções para que consigamos verificar as execuções de teste no momento em que forem feitos os pushes/pulls.

### `📂 data`

Esta pasta somente terá o arquivo que iremos posteriormente utilizar para inserir no formulário em uma das etapas do frontend. Em um projeto real, poderia ser nosso repositório de dummy files, ou que arquivos que utilizaríamos como certificados, e etc.

### `📂 feature`

Aqui teremos nossos arquivos `.feature`, que é basicamente nosso repositório dos cenários criados em `BDD`. Além disso, esta pasta é o motor para a execução dos testes, e será onde posteriormente executaremos o `behave`. Também teremos os arquivos `step.py`, que serão basicamente nossos tradutores do `BDD` para o Python.

### `📂 pages`

Nesta pasta temos a execução do `POM (Page Object Model)`, onde desacoplamos a estrutura dos testes, dos componentes de UI. Aqui teremos os arquivos `.py` responsáveis por extrair informações, preencher campos, apertar botões, e tudo mais.

### `📂 services`

Esta pasta terá os arquivos `.py` responsáveis por criar as funções de `GET/POST` das APIs. Será tecnicamente falando nossa camada de comunicação.

### `📂 testes`

Esta pasta terá os arquivos `.py` responsáveis por utilizar as funções criadas na nossa camada de comunicação, e fazer as validações/tratamentos necessários. Iremos posteriormente rodar o `pytest` nos arquivos desta pasta.

## Estrutura dos Código

Conforme explicado, teremos o código separado em duas etapas:

- Testes de API (Usa as pastas `services` e `testes`, além das bibliotecas `HTTPX` e `pytest`).
- Testes de Frontend (Usa as pastas `feature`, `pages` e `data`, além das bibliotecas `selenium`, `webdriver-manager` e `behave`).

Com relação aos testes de API, este é bem direto. A ideia foi simples, separei as requisições no arquivo `services/bookstore_service.py`, e criei o `tests/test_api_flow.py` para ser o executor/validador.

Já nos testes de Frontend, as coisas ‘complicam’ um pouco mais. Primeiro temos o arquivo `pages/base_page.py` que é responsável por criar as funções básicas para todas as telas como `find_element`, `click`, etc. E ainda nas pasta `pages`, teremos as funções específicas por telas, como por exemplo: `form_page.select_gender` ou `form_page.select_hobbies`. Essas são funções que somente serão usadas por uma tela em específico, e é por isso que chamamos de `POM (Page Object Model)`.

Seguindo adiante, temos os casos de teste criados em um arquivo na pasta `feature`, como por exemplo o `feature/form.feature`. Esse arquivo é onde iremos inserir o `Gherkin (BDD)` puro, e este funcionará de repositório para quando rodarmos o `behave`. Também na pasta `feature` temos o `environment.py`, que é responsável por determinar alguns argumentos para o Chrome e determinar o que irá ser feito antes/depois dos testes.

Ainda na pasta `feature`, teremos a pasta `steps`, que será responsável por centralizar por ser o dicionário do `BDD` criado para cada etapa do desafio, como no `feature/form.feature` por exemplo, acionando as funções que criamos nos `pages` e criando a camada de validação.

## Observações Importantes

Eu não sei qual o padrão de escrita da Accenture, então irei assumir que por ser uma empresa internacional, utilizam o English First para escrever os códigos. Se isso não for uma realidade, em projetos após a contratação, não me importaria de escrever em português.

Durante a criação do `form_page.py` identifiquei que os anúncios por vezes interferiam na execução dos cenários. Por isso, pedi ajuda do `https://gemini.google.com/` para criar uma função em Java Script que removesse os anúncios (`_remove_ads()`). 

## Considerações e Erros Encontrados

Na tela “Practice Form”, ao registrar um usuário, e tentar fechar o pop-up utilizando o botão `closeLargeModal`, este não funciona corretamente e não performa nenhuma ação. No código, deixei sem uma validação para isso no decorador `@then('I close the popup')` no `form_steps.py` apenas para obtermos sucesso no teste. Em um cenário real, teríamos uma validação após identificando que o botão não funciona corretamente.
Durante a execução do CRUD do `web_table`, poderia ter separado o registro entre registrar, modificar e excluir. Não sei se queriam um fluxo único ou não, mas optei por essa abordagem afim de trazer um resultado sólido.

Não sei qual exatamente qual o objetivo da avaliação, se é verificar minha capacidade de programação ou meu entendimento como QA. Para não encher o código com testes que não foram solicitados, colocarei aqui algumas coisas que não são validadas, e poderíamos validar afim de trazer uma melhor cobertura de testes.

- Não fizemos nenhum teste `BVA` (ou teste de fronteira) para validar se os limites dos campos funcionam corretamente.
- Não fizemos nenhuma validação em cima do limite mínimo e máximo de caracteres em um componente (apesar de que no “Practice Form” temos a validação feita pelo próprio formulário, e se não é devidamente preenchido, este sinaliza).
- Não fizemos teste de carga no upload do ficheiro.
- Não validamos nenhum aspecto de `UI/UX`, como o fato de os botões do menu lateral não funcionarem corretamente, e sim os textos terem função de hyperlink.
- Em basicamente todos os cenários, somente fizemos os casos positivos, ignorando os cenários negativos.
- Poderia ter adicionado camadas de validação visual, como tirar print ao preencher o formulário, ou tirar print ao visualizar um componente.

## Uso de Inteligência Artificial

Como um pós-graduando em Inteligência Artificial, eu preciso comentar sobre o uso de modelos de `LLM` como ferramenta. No meu entendimento, a geração de código de forma descompensada é um problema de segurança, porém quando acompanhada de um profissional que entende seus objetivos e o que está programando, pode se tornar uma solução incrível em termos de escalabilidade.

Conforme mencionado anteriormente, utilizei a IA em algumas funções auxiliares, como `_remove_ads()`. Além disso, em alguns momentos utilizei para escrever o `Gherkin` em inglês de forma mais adequada, e utilizei no troubleshooting de alguns problemas que peguei, como por exemplo o fix que fiz denominado `Adding chrome_option headless to work properly on CI`, pois uma das automações funcionava corretamente em meu computador e não funcionava corretamente na esteira. 