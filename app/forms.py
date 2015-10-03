from flask.ext.wtf import Form
from wtforms import TextAreaField, FileField

class InputTextForm(Form):
    chat_text = TextAreaField('chat_text')
    input_file = FileField('input_file')