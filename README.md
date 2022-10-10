# To-Do List App (Advice Health)

To-Do List App
Description
Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

Requirements

● Setup the dev environment with docker
○ Using docker-compose with as many volumes as it takes
● Use Python’s Flask framework and any other library
● Use any SQL database
● Secure routes
● Write tests

Time to deliver, 72 hour

---

## Clone

```bash
git clone https://github.com/escobar-felipe/advice_test
```

## Ambiente

Python 3.10+
Ative a sua virtualenv
set FLAKS_ENV = development

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
pip install -r requirements_test.txt
```

ou 

```bash
make install
```

## Testando

```bash
pytest carford/tests
```
ou 

```bash
make tests
```
## Executando

```bash
flask create-db  # rodar uma vez
flask populate-db # rodar uma vez
flask add-user -u admin -p 1234  # adiciona usuario admin
flask run
```
## Executando container

```bash
docker-compose up --build
```

ou 

```bash
make run
```
Acesse:

- Website: http://localhost:8000
- Admin: http://localhost:8000/admin/
  - user: admin, senha: 1234

## Structure

```bash
.
├── carford (MAIN PACKAGE)
│   ├── app.py (APP FACTORIES)
│   ├── blueprints (BLUEPRINT FACTORIES)
│   │   ├── __init__.py
│   │   ├── restapi (REST API)
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   └── webui (FRONT END)
│   │       ├── __init__.py
│   │       ├── templates
│   │       │   ├── index.html
│   │       │   └── owner.html
│   │       └── views.py
│   ├── development.db
│   ├── ext (EXTENSION FACTORIES)
│   │   ├── admin.py
│   │   ├── appearance.py
│   │   ├── auth.py
│   │   ├── commands.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   ├── forms.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models.py (DATABASE MODELS)
│   ├── production.db
│   ├── static
│   │   ├── img
│   │   │   └── Carford.png
│   │   └── js
│   │       └── functions.js
│   ├── tests (TESTS)
│   │   ├── conftest.py
│   │   ├── functional (FUNCTIONAL TESTS)
│   │   │   ├── __init__.py
│   │   │   └── test_recipes.py
│   │   ├── __init__.py
│   │   └── unit (UNIT TESTS)
│   │       ├── __init__.py
│   │       ├── test_func.py
│   │       └── test_models.py
│   └── wsgi.py
├── docker-compose.yaml
├── Dockerfile (DOCKERFILE)
├── Makefile 
├── requirements_dev.txt
├── requirements_test.txt
├── requirements.txt
└── settings.toml (SETTINGS)

12 directories, 37 files
```
