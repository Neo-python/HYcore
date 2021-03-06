from forms.fields.primary import *
from plugins.HYplugins.form import BaseForm, VM, JsonField
from plugins.HYplugins.form.fields import PhoneField, CodeField


class SMSCodeForm(BaseForm, PhoneField, CodeField, SmsTemplateIdField):
    """短信发送表单"""


class NoticeManagerForm(BaseForm, SmsTemplateIdField):
    params = JsonField(validators=[
        DataRequired(message=VM.say('required', '短信参数'))
    ])


class SMSBatchForm(BaseForm, SmsTemplateIdField):
    """批量发送短信"""

    phone_list = JsonField(validators=[
        DataRequired(message=VM.say('required', '手机号名单'))
    ])

    params = JsonField(validators=[
        DataRequired(message=VM.say('required', '短信参数'))
    ])


class UploadUrlForm(BaseForm):
    """获取上传图片授权地址"""

    genre = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', '图片类型')),
        Length(max=10, message=VM.say('length', '图片类型', 1, 10))
    ])

    suffix = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', '文件类型')),
        Length(max=10, message=VM.say('length', '文件类型', 1, 10))
    ])

    user_uuid = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', '用户编号')),
        Length(max=40, message=VM.say('system_number', '用户编号', 30, 40))
    ])


class GetOpenIdForm(BaseForm):
    """获取open_id"""

    code = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', 'code')),
        # Length(max=10, message=VM.say('length', 'code', 1, 10))
    ])

    port = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', 'port'))
    ])


class PositionDistanceForm(BaseForm):
    """位置计算距离"""
    origin = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', '原点/起始点坐标'))
    ])
    destinations = JsonField(validators=[
        DataRequired(message=VM.say('required', '目标点坐标'))
    ])


class TokenClearForm(BaseForm):
    """清除用户token"""

    uuid = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', '用户编号')),
        Length(max=40, message=VM.say('system_number', '用户编号', 30, 40))
    ])

    port = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', 'port'))
    ])


class GetFactoryToken(BaseForm):
    """获取厂家token"""

    factory_uuid = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', '用户编号')),
        Length(max=40, message=VM.say('length_unite', '用户编号', 40)),
        DataRequired(message=VM.say('required', '用户编号'))
    ])
