# Flask RESTful API project skeleton

This sample project shows our common ways to implement RESTful API server. And use dockerfile to make sure the environment is consistent.

Here is the implementation of a model :User
Sometime, we have many models, which mean to implement one user has many todos.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-RESTful - restful API library.
3. Flask-Script - provides support for writing external scripts.
4. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.
5. PyMySQL - Python MySQL client library.

Project structure:
```
.
├── README.md
├── run_example_app.py
├── api_docs
├── docker
├── tests
│   ├── __init__.py
├── endpoints
│   ├── __init__.py
│   ├── common
│   ├── config
│   └── routers
│      ├── __init__.py
│      └── users
│          ├── __init__.py
│          ├── model.py
│          └── view.py
├── manage.py
├── pip-requirements.txt
└── run_app.py
```

* api_docs - place app's swagger API document.
* docker - place Dockerfile.
* endpoints - holds all endpoints.
* tests - place unittest and functional test here.
* run_app.py - flask application initialization.
* endpoints.configs - all global app settings with different environment.
* endpoints.common - place all shared module.
* manage.py - script for managing application (migrations, server execution, etc.)


## Setup local environment
### `Database (MySQL)`

For an easy and clean setup project launching, we build the environment by following the `docker-compose.yml` file in the project root folder, by running the following two scripts:
```
docker-compose -f docker-compose.yaml build
```
then, launch localdb with docker-compose in background.
```
docker-compose up -d localdb
```

### `App (Server)`
We use `venv` to create an isolated virtual environment.
```
python3.7 -m venv venv
source venv/bin/activate
```

then you have to pip install pipeline packages when developing pipeline scripts.
```
pip install -r pip-requirements.txt
```

## Running 

1. pip install pip-requirements.txt
2. Run following commands when first run:
    1. flask db init
    2. flask db migrate
    3. flask db upgrade
3. Start server by running python run_app.py


## Usage
### Show examples for Users endpoint
POST http://localhost:5000/api/v1/users

REQUEST
```Bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "test-1","email":"test-1@happy.com"}' http://localhost:5000/api/v1/users
```

RESPONSE
```json
{
    "id": 1,
    "name": "test-1",
    "email": "test-1@happy.com"
}
```
GET http://localhost:5000/api/v1/users/1

RESPONSE
```json
{
    "id": 1,
    "name": "test-1",
    "email": "test-1@happy.com"
}
```
DELETE http://localhost:5000/api/v1/users/1

RESPONSE
```json
{
    "id": 1,
    "name": "test-1",
    "email": "test-1@happy.com"
}
```
GET http://localhost:5000/api/v1/users

RESPONSE
```json
{
    "count": 2,
    "users": [
        {
            "id": 2,
            "name": "test-2",
            "email": "test-2@happy.com"
        },
        {
            "id": 3,
            "name": "test-3",
            "email": "test-3@happy.com"
        }
    ]
}
```

GET http://localhost:5000/api/v1/users?name=test-2
```json
{
    "count": 1,
    "users": [
        {
            "id": 2,
            "name": "test-2",
            "email": "test-2@happy.com"
        }
    ]
}
```

### If we need to query by page, we can use limit and offset, for example:
GET http://localhost:5000/api/v1/users?limit=2&offset=0
```json
{
    "count": 2,
    "users": [
        {
            "id": 2,
            "name": "test-2",
            "email": "test-2@happy.com"
        },
        {
            "id": 3,
            "name": "test-1",
            "email": "test-1@happy.com"
        }
    ]
}
```
