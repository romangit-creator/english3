workers = 3

# Уровень логирования
loglevel = 'info'

# Формат логов доступа
access_log_format = '%(h)s %(r)s %(s)s %(b)s %(f)s %(p)s'

# Путь к файлу логов
accesslog = 'gunicorn_access.log'
errorlog = 'gunicorn_error.log'

# Название и порт
bind = '0.0.0.0:8080'

# Использование asyncio-воркера или другого
worker_class = 'eventlet'

# Время ожидания
timeout = 30
