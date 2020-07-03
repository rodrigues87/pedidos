release: python manage.py migrate
web: gunicorn azmel.wsgi --log-file -
worker: python weakup.py
