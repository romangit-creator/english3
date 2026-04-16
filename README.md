
If you are already using Eventlet, we recommend migrating to a different
framework.  For more detail see
https://eventlet.readthedocs.io/en/latest/asyncio/migration.html
  import eventlet
[2026-04-14 04:04:37 +0000] [11] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:37 +0000] [11] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:38 +0000] [11] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:38 +0000] [11] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:39 +0000] [11] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:39 +0000] [11] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:40 +0000] [11] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:40 +0000] [11] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:42 +0000] [12] [INFO] Booting worker with pid: 12
[2026-04-14 04:04:42 +0000] [12] [WARNING] The eventlet worker is DEPRECATED and will be removed in Gunicorn 26.0. Please migrate to gevent, gthread, or another supported worker type.
[2026-04-14 04:04:41 +0000] [11] [ERROR] Can't connect to ('0.0.0.0', 8080)
[2026-04-14 04:04:42 +0000] [10] [INFO] Worker exiting (pid: 10)
[2026-04-14 04:04:42 +0000] [1] [ERROR] Worker (pid:10) exited with code 1.
[2026-04-14 04:04:42 +0000] [1] [ERROR] Control server error: asyncio.run() cannot be called from a running event loop
 * Restarting with stat
https://eventlet.readthedocs.io/en/latest/asyncio/migration.html
/app/.venv/lib/python3.13/site-packages/gunicorn/workers/geventlet.py:23: EventletDeprecationWarning: 
If you are already using Eventlet, we recommend migrating to a different
framework.  For more detail see
Eventlet is deprecated. It is currently being maintained in bugfix mode, and
we strongly recommend against using it for new projects.
  import eventlet
1 RLock(s) were not greened, to fix this error make sure you run eventlet.monkey_patch() before importing any other modules.
[2026-04-14 04:04:43 +0000] [13] [INFO] Starting gunicorn 25.3.0
[2026-04-14 04:04:43 +0000] [13] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:43 +0000] [13] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:44 +0000] [13] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:44 +0000] [13] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:45 +0000] [13] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:45 +0000] [13] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:46 +0000] [13] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:46 +0000] [13] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:47 +0000] [13] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:47 +0000] [13] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:48 +0000] [13] [ERROR] Can't connect to ('0.0.0.0', 8080)
[2026-04-14 04:04:48 +0000] [12] [INFO] Worker exiting (pid: 12)
[2026-04-14 04:04:48 +0000] [1] [ERROR] Worker (pid:12) exited with code 1.
[2026-04-14 04:04:48 +0000] [1] [ERROR] Control server error: asyncio.run() cannot be called from a running event loop
[2026-04-14 04:04:48 +0000] [14] [INFO] Booting worker with pid: 14
[2026-04-14 04:04:48 +0000] [14] [WARNING] The eventlet worker is DEPRECATED and will be removed in Gunicorn 26.0. Please migrate to gevent, gthread, or another supported worker type.
 * Restarting with stat
1 RLock(s) were not greened, to fix this error make sure you run eventlet.monkey_patch() before importing any other modules.
/app/.venv/lib/python3.13/site-packages/gunicorn/workers/geventlet.py:23: EventletDeprecationWarning: 
Eventlet is deprecated. It is currently being maintained in bugfix mode, and
  import eventlet
https://eventlet.readthedocs.io/en/latest/asyncio/migration.html
we strongly recommend against using it for new projects.
If you are already using Eventlet, we recommend migrating to a different
[2026-04-14 04:04:50 +0000] [15] [INFO] Starting gunicorn 25.3.0
[2026-04-14 04:04:50 +0000] [15] [ERROR] Connection in use: ('0.0.0.0', 8080)
framework.  For more detail see
[2026-04-14 04:04:50 +0000] [15] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:51 +0000] [15] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:51 +0000] [15] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:52 +0000] [15] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:53 +0000] [15] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:53 +0000] [15] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:54 +0000] [15] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:54 +0000] [15] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:55 +0000] [15] [ERROR] Can't connect to ('0.0.0.0', 8080)
[2026-04-14 04:04:55 +0000] [14] [INFO] Worker exiting (pid: 14)
[2026-04-14 04:04:55 +0000] [1] [ERROR] Worker (pid:14) exited with code 1.
[2026-04-14 04:04:55 +0000] [1] [ERROR] Control server error: asyncio.run() cannot be called from a running event loop
[2026-04-14 04:04:55 +0000] [16] [INFO] Booting worker with pid: 16
[2026-04-14 04:04:55 +0000] [16] [WARNING] The eventlet worker is DEPRECATED and will be removed in Gunicorn 26.0. Please migrate to gevent, gthread, or another supported worker type.
 * Restarting with stat
/app/.venv/lib/python3.13/site-packages/gunicorn/workers/geventlet.py:23: EventletDeprecationWarning: 
Eventlet is deprecated. It is currently being maintained in bugfix mode, and
we strongly recommend against using it for new projects.
If you are already using Eventlet, we recommend migrating to a different
framework.  For more detail see
https://eventlet.readthedocs.io/en/latest/asyncio/migration.html
  import eventlet
[2026-04-14 04:04:56 +0000] [17] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
1 RLock(s) were not greened, to fix this error make sure you run eventlet.monkey_patch() before importing any other modules.
[2026-04-14 04:04:56 +0000] [17] [INFO] Starting gunicorn 25.3.0
[2026-04-14 04:04:56 +0000] [17] [ERROR] Connection in use: ('0.0.0.0', 8080)
[2026-04-14 04:04:57 +0000] [17] [ERROR] connection to ('0.0.0.0', 8080) failed: [Errno 98] Address already in use
[2026-04-14 04:04:58 +0000] [17] [ERROR] connection to ('0.0.0.0',
