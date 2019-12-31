import os

print('start')
# # core
os.system(
    'cd /home/ubuntu/neo/HYcore/models/HYModels;'
    'git pull;'
    'cd /home/ubuntu/neo/HYcore/plugins/HYplugins;'
    'git pull;'
    '. /home/ubuntu/neo/venvs/core/bin/activate;'
    'cd /home/ubuntu/neo/HYcore;'
    'git pull;'
    'pip install -r requirements.txt;'
    'killall -9 celery;'
    'cd /home/ubuntu/neo/HYcore;'
    'nohup celery -A plugins.private.asynchronous.run_celery:celery worker & \;'
    'python3 /Users/NeoMacMini/work/HY/HYcore/plugins/private/script/database_update.py'
)
# os.system(
#     'cd /home/ubuntu/neo/HYcore/models/HYModels;'
#     'git pull;'
#     'cd /home/ubuntu/neo/HYcore/plugins/HYplugins;'
#     'git pull;'
#     '. /home/ubuntu/neo/venvs/core/bin/activate;'
#     'cd /home/ubuntu/neo/HYcore;'
#     'git pull;'
#     'pip install -r requirements.txt;'
#     'killall -9 celery;'
#     'cd /home/ubuntu/neo/HYcore;'
#     'nohup celery -A plugins.private.asynchronous.run_celery:celery worker &;'
#     'python3 /Users/NeoMacMini/work/HY/HYcore/plugins/private/script/database_update.py;'
# )

print('core complete')

# factory
os.system(
    'cd /home/ubuntu/neo/HYfactory/models/HYModels;'
    'git pull;'
    'cd /home/ubuntu/neo/HYfactory/plugins/HYplugins;'
    'git pull;'
    '. /home/ubuntu/neo/venvs/factory/bin/activate;'
    'cd /home/ubuntu/neo/HYfactory;'
    'git pull;'
    'pip install -r requirements.txt;'
    'uwsgi --reload /home/ubuntu/neo/HYfactory/server.pid;'
)
print('factory complete')

# driver
os.system(
    'cd /home/ubuntu/neo/HYdriver/models/HYModels;'
    'git pull;'
    'cd /home/ubuntu/neo/HYdriver/plugins/HYplugins;'
    'git pull;'
    '. /home/ubuntu/neo/venvs/driver/bin/activate;'
    'cd /home/ubuntu/neo/HYdriver;'
    'git pull;'
    'pip install -r requirements.txt;'
    'uwsgi --reload /home/ubuntu/neo/HYdriver/server.pid;'
)

print('driver complete')
# manager
os.system(
    'cd /home/ubuntu/neo/HYmanager/models/HYModels;'
    'git pull;'
    'cd /home/ubuntu/neo/HYmanager/plugins/HYplugins;'
    'git pull;'
    '. /home/ubuntu/neo/venvs/manager/bin/activate;'
    'cd /home/ubuntu/neo/HYmanager;'
    'git pull;'
    'pip install -r requirements.txt;'
    'uwsgi --reload /home/ubuntu/neo/HYmanager/server.pid;'
)
print('manager complete')
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
