from app import app
from flask import render_template
from  shownoter import re_link, get_links, get_title

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    from .forms import InputTextForm
    form = InputTextForm()
    
    if form.validate_on_submit():
        text_input = form.chat_text.data
        links = re_link(text_input)
        results = list()
        for link in links:
            title = get_title(link)
            markdown = get_links(link = link, title = title)
            results.append(markdown)
        return render_template('index.html', form = form, results = results)
    return render_template('index.html', form = form)
