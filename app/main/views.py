from flask import render_template
from . import main




@main.route('/')
def index():

    '''
    main page view
    '''
    title = 'Pitches'
    return render_template('index.html',title = title)
