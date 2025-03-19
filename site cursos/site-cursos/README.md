## Projeto: Site de Vendas de Cursos

Este projeto é um site de vendas de cursos desenvolvido com Python e Django. O objetivo é fornecer uma plataforma onde os usuários possam se cadastrar, acessar cursos e gerenciar suas compras.

## Requisitos

* Python 3 ou superior - Conferir a versão: `python --version`
* Django 5 ou superior - Conferir a versão: `django-admin --version`
* GIT - Conferir a instalação: `git -v`
* MySQL 8 ou superior - Conferir a versão: `mysql --version`

## Como rodar o projeto baixado

Criar o ambiente virtual.
```
python -m venv venv
```

Ativar o ambiente virtual.
```
venv\Scripts\activate
```

Instalar as dependências.
```
pip install -r requirements.txt
```

Alterar no arquivo "settings.py" as credenciais do banco de dados.

Executar as migrations.
```
python manage.py migrate
```

Rodar o projeto.
```
python manage.py runserver
```

Acessar o site.
```
http://127.0.0.1:8000/
```

Criar um super usuário.
```
python manage.py createsuperuser
```
```
Usuário (leave blank to use 'cesar'): admin
Endereço de email: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
```

Acessar o sistema administrativo.
```
http://127.0.0.1:8000/admin
```

Executar as seeds para cadastrar registros de teste.
```
python manage.py seed_courses
python manage.py seed_about
```

## Sequência para criar o projeto

Criar o ambiente virtual.
```
python -m venv venv
```

Ativar o ambiente virtual.
```
venv\Scripts\activate
```

Gerar o arquivo com as dependências.
Após instalar a dependência, execute o comando abaixo.
```
pip freeze > requirements.txt
```

Instalar o Django.
```
pip install Django
```

Desinstalar o Django.
```
pip uninstall Django
```

Criar o projeto com Django.
```
django-admin startproject admin .
```

Rodar o projeto.
```
python manage.py runserver
```

Acessar o site.
```
http://127.0.0.1:8000/
```

Estrutura do projeto:
```
meu_projeto/
├── manage.py              # Ferramenta CLI para gerenciar o projeto
├── meu_projeto/           # Diretório principal do projeto
│   ├── __init__.py        # Identifica o diretório como um módulo Python
│   ├── settings.py        # Configurações do projeto
│   ├── urls.py            # Rotas principais do projeto
│   ├── asgi.py            # Configuração para ASGI
│   └── wsgi.py            # Configuração para WSGI
```

Executar as migrations.
```
python manage.py migrate
```

Instalar o conector MySQL.
```
pip install mysqlclient
```

Criar a base de dados.
```
CREATE DATABASE celke CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Executar as migrations para criar as tabelas.
```
python manage.py migrate
```

Criar um super usuário.
```
python manage.py createsuperuser
```

Acessar o sistema administrativo.
```
http://127.0.0.1:8000/admin
```

Criar novo app.
```
python manage.py startapp nome-do-app
```
```
python manage.py startapp courses
```

Criar migrations.
```
python manage.py makemigrations --name nome-da-migration
```
```
python manage.py makemigrations --name create_courses
```

Instalar o django-tinymce.
```
pip install django-tinymce
```

Instalar o Bootstrap.
```
pip install django-bootstrap-v5
```

Biblioteca para trabalhar com campos do tipo ImageField.
```
pip install Pillow
```

Após instalar a dependência, execute o comando abaixo.
```
pip freeze > requirements.txt
```

## Como usar o GitHub

Baixar os arquivos do GitHub.
```
git clone -b <branch_nome> <repositorio_url> .
```

Verificar a branch.
```
git branch
```

Baixar as atualizações.
```
git pull
```

Adicionar todos os arquivos modificados para a staging area.
```
git add .
```

Commitar as alterações.
```
git commit -m "Descrição do commit"
```

Enviar os commits locais para um repositório remoto.
```
git push <remote> <branch>
git push origin develop
```

Remover o arquivo do cache do GIT.
```
git rm --cached db.sqlite3
```

Remover o diretório do cache do GIT.
```
git rm --cached -r admin/__pycache__/
```