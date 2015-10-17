from flask.ext.wtf import Form
from wtforms import TextAreaField

class TextInput(Form):
    text_input = TextAreaField('text_input')

