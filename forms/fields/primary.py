import wtforms
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired, Optional
from plugins.HYplugins.form.validators_message import ValidatorsMessage as VM


class SmsTemplateIdField:
    """短信模板编号"""
    template_id = wtforms.StringField(validators=[
        DataRequired(message=VM.say('required', '正文内容编号'))
    ])
