import os

os.system('source /Users/NeoMacMini/work/vevns/HYcore/bin/activate;'
          'cd /Users/NeoMacMini/work/HY/HYcore/plugins/private/alembic;'
          'alembic revision --autogenerate -m "备注";'
          'alembic upgrade head;'
          )