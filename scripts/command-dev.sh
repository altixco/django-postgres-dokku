#!/bin/sh

echo "Installing npm dependencies"
npm install
python manage.py migrate
python manage.py loaddata initial dev
python manage.py runserver 0.0.0.0:8000
