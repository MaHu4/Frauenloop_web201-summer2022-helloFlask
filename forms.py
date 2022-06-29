from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class SampleForm(FlaskForm):
    userName = StringField('Your name', validators=[DataRequired(), Length(min=1, max=80)]) # Requirements for userName: A string mus be entered (StringField); something must be entered (DataRequired), length; STring-field can be replaced by select field etc
    userAge = SelectField('Your Age', validators=[DataRequired(), Length(min=1, max=2)])

    submit = SubmitField('Submit')