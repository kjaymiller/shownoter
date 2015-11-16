from app import app
from app.shownotes import shownotes
from app import shownoter
from app import mongo
from app.forms import TextInput

from flask import render_template, redirect, Markup
import re

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextInput()
     
    if form.validate_on_submit():
        desc = form.description_input.data
        chat_text = form.chat_input.data
        chat_links = map(shownoter.valid_link, shownoter.link_detect(chat_text))
        links = []
        for link in chat_links:
            links.append(shownoter.link(link))
        id = mongo.save_to_db(desc, links)
        
        links_file = shownotes(desc, chat_links)
        links_html = re.sub(r'\n', r'<br>', links_file, re.M)
        return render_template('results.html', links=Markup(links), path=id)

    return render_template('index.html', form=form)

@app.route('/results/<id>')
def results(id):
    result = mongo.retrieve(id)
    description = result['description']
    return render_template('results.html', links=description, path=id)

