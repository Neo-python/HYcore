from forms.fields.primary import *
from plugins.HYplugins.form import BaseForm, VM
from plugins.HYplugins.form.fields import PhoneField, CodeField


class SMSCodeForm(BaseForm, PhoneField, CodeField):
    """短信发送表单"""

    template_id = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', '正文内容编号'))
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
        Length(max=32, message=VM.say('length_unite', '用户编号', 32))
    ])


class GetOpenIdForm(BaseForm):
    """获取open_id"""

    code = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', 'code')),
        # Length(max=10, message=VM.say('length', 'code', 1, 10))
    ])
