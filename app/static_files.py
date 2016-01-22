from app import app
from app.contributors import contributors
from flask import render_template

@app.route('/about')
def about():
    return render_template('about.html',contributors=contributors)

@app.route('/report')
def report():
    return render_template('report.html')


