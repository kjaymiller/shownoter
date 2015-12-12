from flask.ext.wtf import Form
from wtforms import TextAreaField, FileField, StringField

class TextInput(Form):
    chat_input = TextAreaField('text_input')
    file_input = FileField('file_input')

class DescInput(Form):
    title = StringField('title_input')
    description = TextAreaField('text_input')

