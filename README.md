# Media API
Esse repositório deverá conter um exemplo de API para gerenciamento das mídias em vídeo da SambaTech.

## Como rodar a aplicação

### Requisitos

É necessário que estejam instalados devidamente:
- [Git](https://git-scm.com/downloads)
- [Python 3](https://www.python.org/downloads/)
- Gerenciador de pacotes do python, [pip](https://pypi.org/project/pip/)
- [virtualenv](https://pypi.org/project/virtualenv/), ou outra ferramenta para criação de ambientes virtuais do python.

### Obtendo o código fonte

Primeiramente, é necessário obter o código fonte do projeto, realizando o download do projeto ou clonando o projeto ao executar o comando abaixo via linha de comando (é necessário ter o [git](https://git-scm.com/downloads) instalado):

```
git clone https://github.com/GiovanniDias/media-api
```

### Configurando o ambiente

Para isolar a aplicação, as dependências do projeto e as variáveis de ambiente por ele utilizadas do contexto do sistema operacional, iremos configurar um ambiente virtual onde a aplicação irá rodar. 

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

### Executando a aplicação em localhost

Para executar a aplicação em localhost basta executar o comando `flask run`.

Após a inicialização da aplicação, o serviço estará disponível no endereço e porta (por padrão [localhost:5000](localhost:5000/)).