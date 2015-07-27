from app import app
from app import ptshownotes
from .forms import chatImport
from flask import render_template
from flask import Markup

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config.ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = chatImport()
    input_text = str()
    if form.input_file:
        import os
        from request import files
        from werkzeug import secure_filename
        file = files['input_file']
        filename = secure_filename(form.input_file.data)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('index.html', form = form, er_cnt = 0)

    elif input_text:
        links = ptshownotes.Shownotes(form.input_file)
        md_text = links.md_text.split('\n')
        bad_links = links.bad_links
        er_cnt = len(bad_links)
        return render_template('index.html', form = form, md_text = md_text, bad_links = bad_links, er_cnt = er_cnt) 

    return render_template('index.html', form = form, er_cnt = 0)



