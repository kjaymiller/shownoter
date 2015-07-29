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
        bad_links = links.bad_links
        er_cnt = len(bad_links)
        return render_template('index.html', form = form, links = links, bad_links = bad_links, er_cnt = er_cnt)
    
    return render_template('index.html', form = form, er_cnt = 0)

@app.route('/results/delete', methods =  ['GET', 'POST'])

def delete_link(links, category, link):
    links.delete_link(cateogry, link)
    md_text = links.md_text.split('\n')
    bad_links = links.bad_links
    er_cnt = len(bad_links)


@app.route('/download/<path:filename>')
def get_file(filename):
    file_path = 'app/downloads/' + filename, 
    with open('app/downloads/' + filename, 'r') as file:
        response = make_response(file.read())
        response.headers['Content-Disposition'] = 'attachment; filename=' + filename 
        response.content_type =  "text/markdown"
    os.remove('app/downloads/' + filename)
    return response
    

       
