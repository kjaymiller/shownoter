from app import app
from app import ptshownotes
from .forms import chatImport
from flask import render_template
from flask import make_response
from flask import Markup
from flask import request
from flask import send_from_directory
import os

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config.ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = chatImport()
    input_text = str()

    def upload_file():
        file = request.files['input_file']
        file = file.read()
        return file.decode('utf-8')
       
    if request.method == 'POST': 
        if request.files['input_file']:
            from werkzeug import secure_filename
            links = ptshownotes.Shownotes(upload_file())

        elif form.input_text:
            links = ptshownotes.Shownotes(form.input_text.data)

        md_text = links.md_text.split('\n')
        return render_template('index.html', form = form, links = links)
    
    return render_template('index.html', form = form, er_cnt = 0)

@app.route('/results/remove')
def delete_link(filename, link):
    with open(filename, 'r+') as file:
        file = file.read()
    os.remove(filename)
    for line in file.split('\n'):
        if not line.endswith(link):
            new_file += line + '\n'
    links = ptshownotes.Shownotes(md_text = new_file) 
    form = chatImport()
    input_text = str()

    return render_template('index.html', form = form, links = links)
    
@app.route('/download/<path:filename>')
def get_file(filename):
    file_path = 'app/downloads/' + filename, 
    with open('app/downloads/' + filename, 'r') as file:
        response = make_response(file.read())
        response.headers['Content-Disposition'] = 'attachment; filename=' + filename 
        response.content_type =  "text/markdown"
    os.remove('app/downloads/' + filename)
    return response
    

       
