"""周期性任务"""
from celery.task import periodic_task
from celery.schedules import crontab
from plugins.private.asynchronous.primary import db_session


@periodic_task(run_every=crontab(minute='*/5', hour='7-22'))
@db_session
def order_entrust_check():
    """订单委托超时检查
    每5分钟执行一次, 早7点--晚22点
    :return:
    """
