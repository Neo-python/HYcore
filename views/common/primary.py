import config
import uuid
from flask import request
from views.common import api
from init import client, sms, cos_sts, wechat_api, position
from asynchronous import tasks
from forms.common import primary as forms
from models.common import Images
from plugins.HYplugins.common import ordinary
from plugins.HYplugins.error import ViewException


@api.route('/get_open_id/')
def get_open_id():
    """获取open_id"""
    form = forms.GetOpenIdForm(request.args).validate_()
    print(wechat_api.update_access_token())
    return ordinary.result_format(data=wechat_api.get_open_id(form.code.data, port=form.port.data))


@api.route('/upload_url/')
def upload_url():
    """获取上传图片授权地址"""
    form = forms.UploadUrlForm(request.args).validate_()

    if not form.genre.data and not form.suffix.data:
        raise ViewException(error_code=4005, message='<genre>图片用途类型或<suffix>图片文件类型,不能为空.')
    name = uuid.uuid1().hex
    path = f'/test/{name}.{form.suffix.data}'
    url = client.get_presigned_url(config.Bucket, path, Method='POST')
    image_url = f'{config.cos_base_url}{path}'
    Images(user_uuid=form.user_uuid.data, url=image_url, genre=form.genre.data, status=1).direct_commit_()
    return ordinary.result_format(data={'upload_url': url, 'image_url': image_url})


@api.route('/upload_credentials/')
def upload_credentials():
    """腾讯cos上传凭证
    文档:https://github.com/tencentyun/qcloud-cos-sts-sdk/tree/master/python
    """
    result = cos_sts.get_credential()
    data = result['credentials']
    data.update({'expiredTime': result['expiredTime']})
    return ordinary.result_format(data=data)


@api.route('/send_sms/code/', methods=['POST'])
def send_sms():
    """发送短信接口
    params:统一规范 验证码 + 时效(分钟)
    """
    form = forms.SMSCodeForm().validate_()

    # sms.send(template_id=form.template_id.data, phone_number=form.phone.data,
    #          sms_sign='台州海嘉粤运输有限公司',
    #          params=[form.code.data, 5])

    return ordinary.result_format()


@api.route('/send_sms/batch/', methods=['POST'])
def batch_sms():
    """批量发送短信"""

    form = forms.SMSBatchForm().validate_()

    tasks.batch_sms.apply_async(kwargs={
        'template_id': form.template_id.data,
        'phone_list': form.phone_list.data,
        'params': form.params.data
    })

    return ordinary.result_format()


@api.route('/position/distance/', methods=['POST'])
def position_distance():
    """计算位置距离
    origin原点只支持单点
    destinations目标点支持多点
    :return:
    """
    form = forms.PositionDistanceForm().validate_()
    result = position.distance(origin=form.origin.data, destinations=form.destinations.data)

    return ordinary.result_format(data=result)
