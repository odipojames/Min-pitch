from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import main
from .forms import PitchForm, CommentForm
from ..models import Pitch, Comment
from ..auth.forms import RegistrationForm

@main.route('/')
def index():
    '''
    function that returns index and its content
    '''
    form = RegistrationForm()
    return render_template('index.html', registration_form = form)

@main.route('/home')
def home():
    '''
    function that returns root.html page and its content
    '''
    title = 'Home'
    return render_template('root.html', title = title)

@main.route('/pitch/<cat>')
def category(cat):
    '''
    function to return the pitches
    '''
    category = Pitch.get_pitch(cat)
    print(category)
    title = f'{cat}'
    return render_template('pitch.html',title = title, category = category)

@main.route('/new-pitch',methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        cat = form.category.data
        pich = form.pitch.data

        new_pitch = Pitch(category = cat, pitch = pich, user_id = current_user.id)

        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    title = 'New Pitch'
    return render_template('new_pitch.html', title=title, pitch_form = form)

@main.route('/comment/<id>')
def comment(id):
    '''
    function to return the pitches
    '''
    comment = Comment.get_comment(id)
    print(comment)
    title = 'comments'
    return render_template('comment.html',title = title, comment = comment)

@main.route('/new_comment/<int:id>', methods = ['GET', 'POST'])
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():

        com = form.comment.data

        new_comment = Comment(comment = com, user_id = current_user.id, pitchs_id = id)
        new_comment.save_comment()

        return redirect(url_for('main.home'))

    title = 'New Comment'
    return render_template('new_comment.html', title = title, comment_form = form, pitch_id = id)
