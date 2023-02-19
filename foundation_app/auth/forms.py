# Create your forms here.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from foundation_app.extensions import app, db, bcrypt 
from foundation_app.models import User

class SignUpForm(FlaskForm):
    """Form for creating/updating Donor."""
    username = StringField('username:', 
        validators=[
            DataRequired(), 
            Length(min=3, max=30, message="name must be between 3 and 30 chars")
        ]) 
    password = PasswordField('Password', validators=[DataRequired()])
    phone_number = StringField('phone number:', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="address needs to be betweeen 3 and 50 chars")
        ])
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('No user with that username. Please try again.')
        
    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not bcrypt.check_password_hash(
                user.password, password.data):
            raise ValidationError('Password doesn\'t match. Please try again.')
