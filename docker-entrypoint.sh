#!/bin/sh

# apply database migrations
echo "---apply database migrations---"
python manage.py migrate

# load initial data
echo "---apply database migrations---"
python manage.py loaddata fixtures/company.json
python manage.py loaddata fixtures/vacancy.json

# runserver
echo "---run server---"
python manage.py runserver 0.0.0.0:8000
