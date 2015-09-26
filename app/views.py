from app import app
from flask import render_template
from  shownoter import re_link, get_link, get_title, detect_image
from itertools import filterfalse

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    from .forms import InputTextForm
    form = InputTextForm()
    
    if form.validate_on_submit():
        text_input = form.chat_text.data
        links = re_link(text_input)

        #find all images save to images
        images = filter(detect_image(), links)

        #find all websites save to websites
        potential_sites = filterfalse(detect_image(),links)

        #find all websites that failed save to bad_links
        links = [(link, True) for link in validate(potential_sites)]          

        
        def markdownerize(link):
            image = detect_image(link)
            title = get_title(link, image=image)
            markdown = get_link(link=link, title=title, image=image)
            return markdown

        
        
        link_list = filter(None, map(markdownerize, links))
        bad_links = 
        return render_template('index.html', form=form, results=link_list)
    return render_template('index.html', form=form)
