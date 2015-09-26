from app import app
from collections import namedtuple
from flask import render_template
from shownoter import re_link, validate_link, get_title, detect_image, get_markdown
from itertools import filterfalse

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    from .forms import InputTextForm
    form = InputTextForm()
    if form.validate_on_submit():
        text_input = form.chat_text.data
        links = re_link(text_input)
        
        site = namedtuple('site', ['url', 'title'])

        images = filter(detect_image, links)
        potential_sites = {(link, validate_link(link)) for link in links if link not in images}
        sites = {site(link[0], get_title(link[1])) for link in potential_sites if link[1]}

        markdown_images = {get_markdown(image) for image in images}
        markdown_sites = {get_markdown(link.url, title=link.title) for link in sites}
        
        markdown = markdown_sites.union(markdown_images)        

        return render_template('index.html', form=form, results=markdown)
    return render_template('index.html', form=form)
