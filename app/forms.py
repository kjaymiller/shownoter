from flask.ext.wtf import Form
from wtforms import TextAreaField

class InputTextForm(Form):
    text = TextAreaField('input text')
