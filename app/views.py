from app import app
from collections import namedtuple
from flask import render_template, make_response
from flask import request, url_for
from itertools import chain
import shownoter

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    from .forms import InputTextForm
    form = InputTextForm()
    if form.validate_on_submit():
        text_input = form.chat_text.data
        links = shownoter.re_link(text_input) 

        images = list(filter(shownoter.detect_image, links))

        site = namedtuple('site', ['url', 'title'])
        potential_sites = [(link, shownoter.validate_link(link)) for link in links if link not in images]
        print(potential_sites)
        sites = (site(link[0], shownoter.get_title(link[1])) for link in potential_sites if link[1])

        markdown_images = (shownoter.get_markdown(image) for image in images)
        markdown_sites = (shownoter.get_markdown(link.url, title=link.title) for link in sites)
        markdown = list(chain(markdown_sites, markdown_images))        
       
        if 'download' in request.form:
            markdown_list = ''

            for link in markdown:
                markdown_list += link + '\n'

            response = make_response(markdown_list)
            response.headers['Content-Disposition'] = 'attachment; filename=results.txt'
            response.content_type = 'text/plain'
            return response

        return render_template('index.html', form=form, results=markdown)

    return render_template('index.html', form=form)

