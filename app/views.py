from app import app
from app import shownoter
from app import mongo
from app.forms import TextInput

from flask import render_template
from flask import Markup
from flask import flash
from flask import request

import re
from markdown import markdown

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextInput()
     
    if form.validate_on_submit():
        desc = form.description_input.data
        if form.file_input.data:
            flash('file detected')
            file = request.files['file_input']
            chat_text = file.read().decode('utf-8')
        else:
            chat_text = form.chat_input.data
        chat_links = map(shownoter.valid_link, shownoter.link_detect(chat_text))
        db_links =[]
        for link in chat_links:
            db_links.append(shownoter.create_markdown(link, shownoter.title(link)))
        id = mongo.save_to_db(desc, db_links)
        links = shownoter.links_to_string(db_links)
        return render_template('results.html',
                description=desc,
                links=Markup(links),
                path=id,
                download=True)

    return render_template('index.html', form=form)

@app.route('/results/<id>')
def results(id):
    result = mongo.retrieve(id)
    description = result['description']
    links = shownoter.links_to_string(result['links'])
    return render_template('results.html', 
            links=Markup(links), 
            description=description,
            path=id,
            download=False)

