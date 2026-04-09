# NOTAS

## Ambiente Virtual:
Crie um ambiente virtual na pasta Django `python -m venv venv`

**Para ativar o ambiente virtual:** <br>
Execute dentro de Django `venv\Scripts\activate`

**Para desativar o ambiente virtual:**<br>
Execute dentro de Django `deactivate`

## Instalando o Django:
Com o ambiente virtual ativado, dentro da pasta Django, execute `pip install django`

**Confira a versão:** `django-admin --version`

## Novo Projeto Django:
**Comandos essenciais**<br>
* `django-admin startproject nome_projeto .`
* `python manage.py startapp nome_app`
* `python manage.py runserver`

## Variáveis de Ambiente:
1. Na raíz do projeto em questão, crie o arquivo `.env`.
2. Copie o conteúdo de `.env.example` e cole em `.env`.
3. Gere a *Secret Key* do Django e cole como valor da variável **SECRET_KEY** no `.env`
4. Instale o `python-decouple` na pasta Django com o ambiente virtual ativo

**Obs.: Mantenha a variável `DEBUG` com valor `true` no arquivo `.env`.**

## Secret Key do Django:
Para gerar uma nova *Secret Key* no Django, execute o comando

```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copie o resultado e cole no arquivo `.env`.

## Python Decouple:
* Instale o Python-Decouple: `python -m pip install python-decouple`
* Confira a instalação: `python -c "from decouple import config; print('Decouple OK')"`