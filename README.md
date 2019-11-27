# HYcore
核心中台

# celery
- 启动命令


    celery -A plugins.private.asynchronous.run_celery:celery worker
    
# 全项目更新
- 启动命令
    
    
    
    python3 /home/ubuntu/neo/HYcore/plugins/private/script/updata.py                # 更新所有项目
    nohup python3 main.py > core.log &                                              #核心中台挂起命令