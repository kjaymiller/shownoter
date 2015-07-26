from app import app
from app import ptshownotes
from .forms import chatImport
from flask import render_template
from flask import Markup

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = chatImport()
    input_text = str()

    if form.validate_on_submit():
        input_text = form.input_text.data
        links = ptshownotes.Shownotes(input_text)
        md_text = links.md_text.split('\n')
        bad_links = links.bad_links
        er_cnt = len(bad_links)
        return render_template('index.html', form = form, md_text = md_text, bad_links = bad_links, er_cnt = er_cnt) 

    return render_template('index.html', form = form, er_cnt = 0)



