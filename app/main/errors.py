from flask import render_template
from . import main
from .. import db

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    function to render the error 404 page
    '''
    return render_template('error.html'), 404
