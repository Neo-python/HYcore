import os

os.system('. /home/ubuntu/neo/venvs/core/bin/activate;'
          'cd /home/ubuntu/neo/HYcore/plugins/private/alembic;'
          'alembic revision --autogenerate -m "备注";'
          'alembic upgrade head;'
          )