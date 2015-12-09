from app import app
from app import shownoter
from app import mongo
from app import download
from app.forms import TextInput

from flask import render_template
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

        #Detect Links and saves them to list    
        chat_links = shownoter.link_detect(chat_text)
        db_links = []
        errors = []
        for link in chat_links:
            site = shownoter.valid_link(link)
            if not site:
                continue
            url = site.url

            image = shownoter.image_detect(url)
            if not image:
                title = shownoter.title(site)

            db_links.append(shownoter.create_markdown(url, title))
    return render_template('index.html', form=form)

#@app.route('/description', methods=['GET', 'POST'])
#def desc():
#    form = TextInput()
#
#    if form.validate_on_submit():
#        description = form.description_input.data
#
#        shownotes = shownoter.combine_shownotes(
#                description = description,
#                links = shownoter.links_to_string(db_links),
#                html=html)
#
#        #saves information to the MongoDB
#        id = mongo.save_to_db(description, db_links)
#            results=Markup(shownotes),
#            path=id,
#            html=html)
#                
#
#    return render_template('index.html', form=form)

@app.route('/results/<id>', methods=['GET', 'POST'])
def results(id, html):
    result = mongo.retrieve(id)
    shownotes = shownoter.combine_shownotes(
            description=result['description'],
            links=shownoter.links_to_string(result['links']),
            html=html)
    
    return render_template('results.html', 
            results=Markup(shownotes), 
            path=id,
            )

@app.route('/download/<id>', methods=['GET'])
def download_file(id):
    result = mongo.retrieve(id)
    shownotes = shownoter.combine_shownotes(
            description=result['description'],
            links=shownoter.links_to_string(result['links']),
            html=False)

    response = make_response(shownotes)
    response.headers['Content-Disposition'] = 'attachment; filename=results.txt'
    response.content_type = 'text/plain'
    return response
