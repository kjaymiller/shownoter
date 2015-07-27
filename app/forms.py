from flask.ext.wtf import Form
import wtforms
from wtforms.validators import DataRequired

class chatImport(Form):
    input_text = wtforms.TextAreaField('text')
    input_file = wtforms.FileField()
    
