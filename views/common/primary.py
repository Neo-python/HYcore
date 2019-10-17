import config
import uuid
from flask import request, g
from views.common import api
from init import client, Redis, sms, cos_sts, wechat_api
from forms.common import primary as forms
from models.common import Images
from plugins.HYplugins.common import ordinary
from plugins.HYplugins.error import ViewException


@api.route('/get_open_id/')
def get_open_id():
    """获取open_id"""
    form = forms.GetOpenIdForm(request.args).validate_()
    return ordinary.result_format(data=wechat_api.get_open_id(form.code.data))


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

    sms.send(template_id=form.template_id.data, phone_number=form.phone.data,
             sms_sign='台州海嘉粤运输有限公司',
             params=[form.code.data, 5])

    return ordinary.result_format()
