"""
apply_async
"""
from init import celery, sms
from plugins.private.asynchronous.primary import db_session


@celery.task()
@db_session
def batch_sms(template_id: str, phone_list: list, params: list):
    """批量发送短信"""

    for phone in phone_list:
        sms.send(template_id=template_id, phone_number=phone, sms_sign='台州海嘉粤运输有限公司', params=params)
