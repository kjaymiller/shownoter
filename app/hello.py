import forms
from flask import Flask
from flask import render_template

config.from_object('config')
app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    form = forms.chat()
    return render_template('base.html', name = 'jay', form = form)

if __name__ == '__main__':
    app.run(debug = True)
