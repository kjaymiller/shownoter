from app import app
from app import shownoter
from app import mongo
from app import download
from app.contributors import contributors
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
            flash('Enter any description or other text for your notes')
            file = request.files['file_input']
            chat_text = file.read().decode('utf-8')

        elif form.chat_input.data:
            chat_text = form.chat_input.data

        else:
            flash('no chat detected')
            return render_template('index.html', form=form)

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
                'description': form.description.data
            }
        mongo.append_to_entry(id, entry)

        return redirect(url_for('results', id=id))
    return render_template('links.html', form=form, links=links)

@app.route('/results/<id>', methods=['GET','POST'])
def results(id):
    db_entry = mongo.retrieve(id)
    description = Markup(markdown(db_entry['description']))
    links = [link for link in db_entry['links']]
    title = db_entry['title']
    return render_template('results.html',
            title=title,
            description=description,
            links=links,
            id=id)


@app.route('/download/<id>', methods=['GET'])
def download_file(id):
    db_entry = mongo.retrieve(id)
    description = db_entry['description']
    links = [link['markdown'] for link in db_entry['links']]
    link_text = ''

    for link in links:
        link_text += link + '\n'

    title = db_entry['title']

    if title:
        title = "#" + title

    file = '''{title}
{description}
##Links
{links}'''.format(title=title, description=description, links=link_text)

    if title:
        filename = title + '.txt'
    else:
        filename = 'untitled.txt'

    response = make_response(file)
    response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    response.content_type = 'text/plain'
    return response

@app.route('/about')
def about():
    return render_template('about.html', contributors=contributors)

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/404')
def fourzerofour():
    return render_template('404.html')
