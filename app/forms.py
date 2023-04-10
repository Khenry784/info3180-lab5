# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField,validators,TextAreaField,SelectField,FileField
from wtforms.validators import InputRequired,DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from random import choices


class MovieForm(FlaskForm):
    title = StringField('Movie Title',validators=[DataRequired()])
    description= TextAreaField('Description',validators=[DataRequired()])
    poster=FileField('Movie Poster', validators=[FileRequired('No photo was submitted.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])