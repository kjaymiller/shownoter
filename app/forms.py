from flask.ext.wtf import Form
from wtforms import TextAreaField, FileField, StringField, BooleanField


class TextInput(Form):
    chat_input = TextAreaField('text_input')
    file_input = FileField('file_input')
    custom_title = BooleanField('custom_input')
    bypass_title_description = BooleanField('bypass_title_description')


class DescInput(Form):
    title = StringField('title_input')
    description = TextAreaField('text_input')
