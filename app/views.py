from app import app
from app import shownoter
from app import mongo
from app import download
from app.forms import TextInput, DescInput

from flask import render_template, url_for
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

        chat_links = shownoter.link_detect(chat_text)
        links = [] 
        for link in chat_links:
            
            if shownoter.image_detect(link):
                links.append(shownoter.Image(link))
                
            else:
                links.append(shownoter.Link(link))
                    
        return render_template('links.html', links=links, form=DescInput())
    
    return render_template('index.html', form=form)

@app.route('/links', methods=['GET', 'POST'])
def get_links():
    form = DescInput()
    
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        shownotes_id=mongo.save_to_db(
                description = description,
                title = title,
                links = links)
        path=url_for('results', shownotes=shownotes_id)
    
    return render_template('links.html', form=form)

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
