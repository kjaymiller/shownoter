from flask.ext.wtf import Form
from wtforms import TextAreaField

class InputTextForm(Form):
    chat_text = TextAreaField('chat text')
