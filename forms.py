from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class SampleForm(FlaskForm):
    userName = StringField('Your name', validators=[DataRequired(), Length(min=1, max=80)]) # Requirements for userName: A string mus be entered (StringField); something must be entered (DataRequired), length; STring-field can be replaced by select field etc
    userAge = IntegerField('Your Age', validators=[DataRequired()])
    # # email = StringField('Your Email', [Email(message=('Not a valid email address.'))DataRequired()]

    submit = SubmitField('Submit')