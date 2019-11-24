#!/bin/bash
import os

print('start')
# core
# 'uwsgi --reload /home/ubuntu/neo/HYcore/server.pid;'
os.system('cd /home/ubuntu/neo/HYcore/models/HYModels;'
          'git pull;'
          'cd /home/ubuntu/neo/HYcore/plugins/HYplugins;'
          'git pull;'
          'source /home/ubuntu/neo/venvs/core/bin/activate;'
          )

print('core complete')

# factory
os.system(
    'cd /home/ubuntu/neo/HYdriver/models/HYModels;'
    'git pull;'
    'cd /home/ubuntu/neo/HYdriver/plugins/HYplugins;'
    'git pull;'
    'source /home/ubuntu/neo/venvs/driver/bin/activate;'
    'uwsgi --reload /home/ubuntu/neo/HYdriver/server.pid;'
)
print('core factory')

# driver
os.system(
    'cd /home/ubuntu/neo/HYdriver/models/HYModels;'
    'git pull;'
    'cd /home/ubuntu/neo/HYdriver/plugins/HYplugins;'
    'git pull;'
    'source /home/ubuntu/neo/venvs/driver/bin/activate;'
    'uwsgi --reload /home/ubuntu/neo/HYdriver/server.pid;'
)

print('core driver')
# manager
os.system(
    'cd /home/ubuntu/neo/HYmanager/models/HYModels;'
    'git pull;'
    'cd /home/ubuntu/neo/HYmanager/plugins/HYplugins;'
    'git pull;'
    'source /home/ubuntu/neo/venvs/manager/bin/activate;'
    'uwsgi --reload /home/ubuntu/neo/HYmanager/server.pid;'
)
print('core manager')
# celery
os.system(
    'killall -9 celery;'
    'cd /home/ubuntu/neo/HYcore;'
    'nohup celery -A plugins.private.asynchronous.run_celery:celery worker &'
)
print('core celery')
# os.system(
#     'cd /home/ubuntu/neo/HYcore/models/HYModels;'
#     'git pull;'
#     'cd /home/ubuntu/neo/HYcore/plugins/HYplugins;'
#     'git pull;'
#     'source /home/ubuntu/neo/venvs/core/bin/activate;'
#     # 'uwsgi --reload /home/ubuntu/neo/HYcore/server.pid;'
#
#     # factory
#     'cd /home/ubuntu/neo/HYfactory/models/HYModels;'
#     'git pull;'
#     'cd /home/ubuntu/neo/HYfactory/plugins/HYplugins;'
#     'git pull;'
#     'source /home/ubuntu/neo/venvs/factory/bin/activate;'
#     'uwsgi --reload /home/ubuntu/neo/HYfactory/server.pid;'
#
#     # driver
#     'cd /home/ubuntu/neo/HYdriver/models/HYModels;'
#     'git pull;'
#     'cd /home/ubuntu/neo/HYdriver/plugins/HYplugins;'
#     'git pull;'
#     'source /home/ubuntu/neo/venvs/driver/bin/activate;'
#     'uwsgi --reload /home/ubuntu/neo/HYdriver/server.pid;'
#
#     # manager
#     'cd /home/ubuntu/neo/HYmanager/models/HYModels;'
#     'git pull;'
#     'cd /home/ubuntu/neo/HYmanager/plugins/HYplugins;'
#     'git pull;'
#     'source /home/ubuntu/neo/venvs/manager/bin/activate;'
#     'uwsgi --reload /home/ubuntu/neo/HYmanager/server.pid;'
#
#     # celery -A plugins.private.asynchronous.run_celery:celery worker
#     'killall -9 celery;'
#     'cd /home/ubuntu/neo/HYcore;'
#     'nohup celery -A plugins.private.asynchronous.run_celery:celery worker &'
#
#     # 'nohup celery beat -A run_celery:celery > beat.out &'
#
# )
print('end')
