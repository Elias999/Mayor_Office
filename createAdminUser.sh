#!/bin/bash

virtualenv env
source env/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
