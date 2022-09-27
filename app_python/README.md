# Moscow-Time application

Shows you current time in Moscow.

## Table of contents

- [Quick start](#quick-start)
- [What's included](#whats-included)
- [Docker](#docker)
- [Unit tests](#unit-tests)
- [Git Actions CI](#git-actions-cI)
- [Copyright and license](#copyright-and-license)

## Quick start

Just clone the repo and run `app_python/moscowtime/manage.py runserver`

## What's included

This repo includes a Django project consisting of a single app. This app provides page with current Moscow time.

## Docker

This application is published to docker hub. To run it use:
```
docker pull ivan239/devops-labs
docker run ivan239/devops-labs
```

## Unit tests
Run application unit tests with:
```
app_python/moscowtime/manage.py test
```

## Git Actions CI
This repository uses Github Ci with 2 jobs:
- `Build_and_test` - builds, lints and tests the application
- `Docker_push` - logins and pushes app image to dockerhub

To test an image published through CI use:
```
docker pull ivan239/moscowtime
docker run ivan239/moscowtime
```

## Copyright and license

Code and documentation copyright 2022 Ivan Obraztsov. Code released under the MIT License.
