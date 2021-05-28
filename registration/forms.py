from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    again_password = PasswordField('Again enter Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')