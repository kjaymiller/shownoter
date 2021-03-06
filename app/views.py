from app import app

# static files
from app import static_files

from app.mongo import shownotes_coll, links_coll
from app.mongo import retrieve_from_db, create_entry, count_entries
from app.mongo import append_to_entry, last_five

from app.views_helper import shownoter_wrapper

from app.forms import TextInput, DescInput

from datetime import datetime
from flask import render_template, url_for, redirect
from flask import Markup
from flask import flash
from flask import request
from flask import make_response

from markdown import markdown


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """This is the home page"""

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

        custom_title = form.custom_title.data
        links = shownoter_wrapper(chat_text,
                                  custom_title_enabled=custom_title)

        link_id = create_entry(value={
                                    'links': links,
                                    'created': datetime.utcnow()
                                    }, collection=shownotes_coll)

        if form.bypass_title_description.data:
            title = 'Untitled Shownotes'

            entry = {
                'title': title,
                'description': ''
                }
            append_to_entry(link_id, entry)
            return redirect(url_for('results', id=link_id))

        else:
            return redirect(url_for('get_links', id=link_id))

    # Retrieves the Stats for the frontpage
    stats = {
        'total_shownotes': count_entries(
            shownotes_coll), 'total_links': count_entries(
            links_coll), 'last_five': [
                (result['title'],
                 result['_id']) for result in last_five()
                ]
        }

    return render_template('index.html', form=form, stats=stats)


@app.route('/links/<id>', methods=['GET', 'POST'])
def get_links(id):
    """This page is where the Title and Description are added"""

    form = DescInput()
    links = [link for link in retrieve_from_db(value=id,
                                               collection=shownotes_coll
                                               )['links']]

    if form.validate_on_submit():
        title = form.title.data
        if not title:
            title = 'untitled shownotes'

        entry = {
                'title': title,
                'description': form.description.data
            }
        append_to_entry(id, entry)

        return redirect(url_for('results', id=id))
    return render_template('links.html', form=form, links=links)


@app.route('/results/<id>', methods=['GET', 'POST'])
def results(id):
    """The final result of creating Shownotes"""

    db_entry = retrieve_from_db(value=id, collection=shownotes_coll)
    description = Markup(markdown(db_entry['description']))
    links = [link for link in db_entry['links']]
    title = db_entry['title']
    if not title:
        title = 'Untitled'
    return render_template('results.html',
                           title=title,
                           description=description,
                           links=links,
                           id=id)


@app.route('/download/<id>', methods=['GET'])
def download_file(id):
    """Saves the file into a .txt file"""

    db_entry = retrieve_from_db(value=id, collection=shownotes_coll)
    description = db_entry['description']
    links = [link['markdown'] for link in db_entry['links']]
    link_text = ''

    for link in links:
        link_text += link + '\n'

    title = db_entry['title']
    file = '''#{title}
{description}
##Links
{links}'''.format(title=title, description=description, links=link_text)

    if title:
        filename = title + '.txt'
    else:
        filename = 'untitled.txt'

    response = make_response(file)
    response.headers[
        'Content-Disposition'] = 'attachment; filename={}'.format(filename)
    response.content_type = 'text/plain'
    return response
