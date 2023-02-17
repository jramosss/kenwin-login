# Kenwin Login

[![codecov](https://codecov.io/gh/jramosss/kenwin-login/branch/master/graph/badge.svg?token=IREQIZE7OW)](https://codecov.io/gh/jramosss/kenwin-login)

## Prerequisites
- python3
- docker-compose

## Install

- Install requirements
  - `pip install -r requirements.txt`
- Start the database service
  - Replace the environment variables `POSTGRES_DB` and `POSTGRES_PASSWORD`
  - `docker-compose up`
- Create the database
  - `python manage.py migrate`
- Create a user
  - `python manage.py createsuperuser`

## Run
`python manage.py runserver`

## Test
`pytest`

## API
- `GET /auth/login/`
- `GET /auth/logout/`


## Why's?
- Why Django?
  - Django is the framework i feel most comfortable with.
- Why Rest Framework?
  - I could have used Django's built in views, but i wanted to use the Rest Framework because i wanted to use the Token Authentication, and not just make and endpoint that opens a door, so i could test it further.