from flask import render_template,redirect
from . import main




@main.route('/')
def root():

    '''
    main page view
    '''
    message= 'Pitches'
    return render_template('root.html',message = message)
