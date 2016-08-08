#!/usr/bin/env bash

docker build -t solveit .

docker run -p 8000:8000 -d solveit bash -c "python manage.py runserver 0.0.0.0:8000"
