# Media API
Esse repositório contém uma API de exemplo para gerenciamento das mídias em vídeo da SambaTech.

## Como rodar a aplicação

### Requisitos

É necessário que estejam instalados devidamente:
- [Git](https://git-scm.com/downloads)
- [Python 3](https://www.python.org/downloads/)
- Gerenciador de pacotes do python, [pip](https://pypi.org/project/pip/)
- [virtualenv](https://pypi.org/project/virtualenv/), ou outra ferramenta para criação de ambientes virtuais do python.

### Obtendo o código fonte

Primeiramente, é necessário obter o código fonte do projeto, realizando o [download do projeto](https://github.com/GiovanniDias/sambatech-media-api/archive/master.zip) ou clonando o projeto ao executar o comando abaixo via linha de comando (é necessário ter o [git](https://git-scm.com/downloads) instalado):

```
git clone https://github.com/GiovanniDias/sambatech-media-api
```

### Configurando o ambiente

Para isolar a aplicação, as dependências do projeto e as variáveis de ambiente por ele utilizadas no contexto da aplicação, iremos configurar um ambiente virtual onde a esta irá rodar. 

_Os passos a seguir consideram você já tem Python 3, pip e virtualenv instalados._

Para configurar a aplicação, precisamos criar e ativar um ambiente virtual, para isso acesse a raiz do diretório do projeto e execute os comandos:

```
python3 -m virtualenv venv
source venv/bin/activate
```

**No Windows**:
```
source venv/Scripts/activate
```

Em seguida, instale as dependências do projeto executando o comando:

```
pip install -r requirements.txt
```

### Configurando a aplicação
Para configurar a aplicação, crie um arquivo chamado `settings.toml` e copie para ele o conteúdo do arquivo `settings_sample.toml`. O arquivo _sample_ contém o nome das variáveis de configuração utilizadas no app, porém o valor dessas variáveis deve ser preenchido de acordo com o contexto em que será executado.

O arquivo `settings.toml` é reconhecido pelo `Dynaconf` que carrega as varíaveis de configuração na inicialização da aplicação.

**OBS:** as varíaveis de ambiente de teste ques estão atribuídas estão de acordo com os valores esperados nos testes configurados, alterá-las pode causar erro na execução dos testes.


### Criando base de dados

Para gerenciar a base de dados localmente, utilize os comandos abaixo:

```
// Criar base de dados
flask create-db


// Remover base de dados
flask drop-db

// Recriar a base de dados
// (drop-db seguido de create-db)
flask recreate-db
```

### Executando a aplicação em localhost

Para executar a aplicação em localhost, será necessário definir a varíavel de ambiente `FLASK_APP`. Para isso basta executar o comando:

```
FLASK_APP=app:create_app flask run
```

Alternativamente, é possível atribuir a variável `FLASK_APP` utilizando um arquivo .env, ou ainda [declarar a varíavel de ambiente no contexto da aplicação](https://flask.palletsprojects.com/en/1.1.x/cli/)

Após a inicialização da aplicação, o serviço estará disponível no endereço e porta (por padrão [localhost:5000](localhost:5000/)).

### Executando testes unitários

Para executar os testes unitários de forma geral, execute o comando `pytest`.