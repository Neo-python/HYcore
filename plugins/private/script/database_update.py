import os

os.system('source /home/ubuntu/neo/vevns/core/bin/activate;'
          'cd /home/ubuntu/neo/HYcore/plugins/private/alembic;'
          'alembic revision --autogenerate -m "备注";'
          'alembic upgrade head;'
          )