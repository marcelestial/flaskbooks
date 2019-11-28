from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, URL
from flaskBooks.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
    						validators=[DataRequired(), 
    						Length(min=2, max=20)])
    email = StringField('Email',
    						validators=[DataRequired(), 
    						Email()]) 
    password = PasswordField('Password',
    						validators=[DataRequired(), 
    						Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
    						validators=[DataRequired(), 
    						Length(min=8), 
    						EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email address is already in use. Please use a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
    						validators=[DataRequired(), 
    						Email()])
    password = PasswordField('Password',
    						validators=[DataRequired(), 
    						Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),
                                Length(max=100)])
    author = StringField('Author', validators=[DataRequired(),
                                Length(max=50)])
    description = TextAreaField('Summary', validators=[DataRequired()])
    isbn = StringField('ISBN (optional)')
    imgurl = StringField('Image URL (optional)')
    submit = SubmitField('Submit Book')