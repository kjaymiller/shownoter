"""
This module handles all of the error routing for shownoter
author: kjaymiller
date created: January 21, 2016 
last modified: January 21, 2016
"""

from app import app
from flask import render_template

@app.errorhandler(404)
@app.errorhandler(500)
def not_found(error):
    return render_template('404.html'), 404

