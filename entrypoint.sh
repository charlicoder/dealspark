#!/bin/bash

python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatic --noinput
gunicorn core.wsgi --timeout 180 --workers 2  --bind 0.0.0.0:8000 --log-level=error
