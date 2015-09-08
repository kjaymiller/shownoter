from app import app
from flask import render_template

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    from .forms import InputTextForm
    form = InputTextForm()
    
    if form.validate_on_submit():
        text_input = form.chat_text.data
        result = re_link(text_input)
        render_template('index.html', form = form, result = result)
    return render_template('index.html', form = form)
