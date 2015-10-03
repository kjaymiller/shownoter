from app import app
from app.download import download
from app.markdownerize import markdownerize
from flask import render_template, make_response, request


def upload_file():
        file = request.files['input_file']
        file = file.read()
        return file.decode('utf-8')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(results = ''):
    from .forms import InputTextForm
    form = InputTextForm()

    if form.validate_on_submit():
        if form.input_file:
            text_input = upload_file()
        else:
            text_input = form.chat_text.data

        markdown = markdownerize(text_input)

        if 'download' in request.form:
            markdown_list = ''
            return download(markdown)
            
        return render_template('index.html', form=form, results=markdown)

    return render_template('index.html', form=form)

