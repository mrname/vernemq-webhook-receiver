#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput

#gunicorn --bind=0.0.0.0 vernemq_webhook_receiver.wsgi
python manage.py runserver 0.0.0.0:8000
