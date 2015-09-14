from app import app
from flask import render_template
from  shownoter import re_link

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    from .forms import InputTextForm
    form = InputTextForm()
    
    if form.validate_on_submit():
        text_input = form.chat_text.data
        results = re_link(text_input)
         
        return render_template('index.html', form = form, results = results)
    return render_template('index.html', form = form)
