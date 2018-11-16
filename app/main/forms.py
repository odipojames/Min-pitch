from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = SelectField(u'Pitch Category', choices=[('business', 'business'), ('pick-up', 'pick-up'), ('interview', 'interview')])
    pitch = TextAreaField('Your Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Your Comment')
    submit = SubmitField('Post')
