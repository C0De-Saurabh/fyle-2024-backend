# Fyle Backend Challenge 2024

## Installation (WINDOWS PowerShell)

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below


### Install requirements

```
virtualenv env
env/scripts/activate
pip install -r requirements.txt
```
### Reset DB

```
$ENV:FLASK_APP="core/server.py"
del core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
flask run
```
### Run Tests

```

# for test coverage report
# pytest --cov

```
## Creating Docker Image
1.Create Dockerfile inside directory
2.Add the commands :
```
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP="core/server.py"

RUN flask db upgrade -d core/migrations/

CMD ["flask", "run", "--host=0.0.0.0"]
```

3.Run the command in terminal to create Docker image 
```
docker build -t fyle-backend .
```
4.Run the command to run image-container(Make Sure you have Docker-Desktop and it is running) (port can be changed as well).
```
docker run -p 5000:5000 fyle-backend
```



## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below
### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```

