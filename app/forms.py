from flask.ext.wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class chatImport(Form):
    input_text = TextAreaField('text', validators=[DataRequired()])
    

    
