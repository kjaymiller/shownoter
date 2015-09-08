from app import app
from flask import render_template

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    from .forms import InputTextForm
    form = InputTextForm()
    return render_template('index.html', form = form)
