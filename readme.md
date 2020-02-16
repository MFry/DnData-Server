## Getting Started

### Quick Run

```bash
python manage.py runserver 0.0.0.0:8000
```

### Setup

```bash
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
```

## Test

```bash
coverage run --source='.' manage.py test

# show report
coverage html

# see report in cli
coverage report
```

## Auth

### Getting a token

```bash
curl -X POST -d "username=username&password=password" http://localhost:8000/auth
```
