from app import app
from app import shownoter
from app import mongo
from app import download
from app.forms import TextInput, DescInput

from flask import render_template, url_for, redirect
from flask import Markup
from flask import flash
from flask import request
from flask import make_response

import re
from markdown import markdown



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextInput()

    if form.validate_on_submit():

        if form.file_input.data:
            flash('file detected')
            file = request.files['file_input']
            chat_text = file.read().decode('utf-8')

        else:
            chat_text = form.chat_input.data

        links = shownoter.format_links_as_hash(chat_text)
        link_id = mongo.create_entry(links)
        return redirect(url_for('get_links', id=link_id))

    return render_template('index.html', form=form)

@app.route('/links/<id>', methods=['GET', 'POST'])
def get_links(id):
    form = DescInput()
    links = [link for link in mongo.retrieve(id)['links']]

    if form.validate_on_submit():
        entry = {
                'title':form.title.data,
                'description':form.description.data
            }
        mongo.append_to_entry(id, entry)

        return redirect(url_for('results', id=id))
    return render_template('links.html', form=form, links=links)

@app.route('/results/<id>', methods=['GET','POST'])
def results(id):
    db_entry = mongo.retrieve(id)
    description = db_entry['description']
    db_links = [link['markdown'] for link in db_entry['links']]
    links = shownoter.links_to_string(db_links)
    title = db_entry['title']
    return render_template('results.html',
            title=title,
            description=description,
            links=Markup(links))


@app.route('/download/<shownotes>', methods=['GET'])
def download_file(shownotes):
    result = mongo.retrieve(shownotes)
    file = shownoter.combine_shownotes(
            description=result['description'],
            links=shownoter.links_to_string(result['links']),
            html=False)
    filename = result['title']+'.txt'
    filename.replace(':','-')
    response = make_response(file)
    response.headers['Content-Disposition'] = 'attachment; filename=results.txt'
    response.content_type = 'text/plain'
    return response
