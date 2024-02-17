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

## Technology that i used 

1. Project manager [Poetry](https://python-poetry.org/)

2. Cache [Redis](https://redis.io/)

3. Dockerize all with [Docker](https://www.docker.com/)

4. Framework [FastAPI](https://fastapi.tiangolo.com/)

5. Database async sessions with [SqlAlchemy](https://www.sqlalchemy.org/)

6. Migrations with [Alembic](https://alembic.sqlalchemy.org/en/latest/)

## TODO

- Add type hints

- Rewrite Dockerfile

- Add Celery for scheduale tasks (like delete referal code after expiration ends, etc.)

- Add Pre-commit hooks for linting project

- Add Makefile for project

- Clean project