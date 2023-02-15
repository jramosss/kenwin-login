# Kenwin Login

[![codecov](https://codecov.io/gh/jramosss/kenwin-login/branch/master/graph/badge.svg?token=IREQIZE7OW)](https://codecov.io/gh/jramosss/kenwin-login)

## Prerequisites
- python3
- docker-compose

## Install

- Install requirements
  - `pip install -r requirements.txt`
- Start the database service
  - `docker-compose up`
- Create the database
  - `python manage.py migrate`

## Run
`python manage.py runserver`

## Test
`pytest`

## API
- `GET /auth/login/`
- `GET /auth/logout/`

