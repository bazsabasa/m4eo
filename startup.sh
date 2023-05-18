#/bin/sh
gunicorn -w 1 wsgi:app --bind 0.0.0.0:8080