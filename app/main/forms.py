from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    pitch = TextAreaField('Generate your Pitch', validators=[Required()])
    my_category = SelectField('Genre', choices=[('Inspirational-Stories', 'Inspirational Stories'), ('Technology', 'Technology'), ('Entrepreneurship', 'Entrepreneurship'), (
        'Cars-Enthusiasim', 'Cars Enthusiasim'), ('Pun-Talent-Sports-Entertainment', 'Pun,Talent,Sports and Entertainment')], validators=[Required()])
    submit = SubmitField('Pitch It!')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about yourself',
                        validators=[Required()])
    submit = SubmitField('Submit')
