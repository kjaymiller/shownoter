from flask.ext.wtf import Form
from wtforms import TextAreaField

class TextInput(Form):
    description_input = TextAreaField('text_input')
    chat_input = TextAreaField('text_input')

