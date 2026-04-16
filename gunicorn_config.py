import os

workers = 1          # для eventlet рекомендуется 1 воркер
worker_class = 'eventlet'
timeout = 30
loglevel = 'info'
access_log_format = '%(h)s %(r)s %(s)s %(b)s %(f)s %(p)s'
accesslog = 'gunicorn_access.log'
errorlog = 'gunicorn_error.log'

# Берём порт из переменной окружения, по умолчанию 8080
port = os.environ.get('PORT', '8080')
bind = f'0.0.0.0:{port}'
