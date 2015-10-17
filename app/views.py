from app import app
from app.forms import TextInput
from flask import render_template, redirect
 

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextInput()
    
    if form.validate_on_submit():
        text = form.text_input.data
        return render_template('results.html', links=text)

    return render_template('index.html', 
                            form=form)

@app.route('/results')
def results(links):
    return links
