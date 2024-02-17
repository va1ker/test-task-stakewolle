## Requirements

1. Python ^3.11

1. [Poetry](https://python-poetry.org/)

3. [Docker](https://www.docker.com/)


## Start Project

Clone the repository

```bash 
git clone
```
Enter into project folder 

```bash
cd folder
```
There is no sensitive information in .env(like tokens, emails, etc.), so you can edit it as you wish

Run project

```bash
docker-compose up --build
```

## Test your API
After starting the project, go to http://localhost:8080/docs <br>
There you see all avaliable endpoints, click "Try it out", and now you can make request to them.

## TODO

- Add type hints

- Rewrite Dockerfile

- Add Celery for scheduale tasks (like delete referal code after expiration ends, etc.)

- Add Pre-commit hooks for linting project

- Add Makefile for project