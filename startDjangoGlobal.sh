#!/bin/bash

virtualenv env
source env/bin/activate
pip3 install asgiref
pip3 install autopep8
pip3 install Django==3.1.*
pip3 install pycodestyle
pip3 install pytz
pip3 install sqlparse
pip3 install Unipath
pip3 install dj-database-url
pip3 install python-decouple
pip3 install gunicorn
pip3 install whitenoise
pip3 install django_extensions
pip3 install django.db
pip3 install django-autoslug
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
