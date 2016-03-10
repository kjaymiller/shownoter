from flask.ext.wtf import Form
from wtforms import TextAreaField, FileField, StringField, BooleanField


class TextInput(Form):
    chat_input = TextAreaField('text_input')
    file_input = FileField('file_input')
    markdown_mode = BooleanField('markdown_mode')


class DescInput(Form):
    title = StringField('title_input')
    description = TextAreaField('text_input')
