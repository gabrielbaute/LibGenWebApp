from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, Optional
import email_validator

# Opciones para los select fields
languages = [('English', 'English'), ('Spanish', 'Spanish'), ('Italian', 'Italian'), ('Portuguese', 'Portuguese'), ('French', 'French'), ('German', 'German')]
extensions = [('pdf', 'PDF'), ('epub', 'EPUB'), ('mobi', 'MOBI'), ('djvu', 'DJVU'), ('lit', 'LIT')]

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AuthorSearchForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    year = IntegerField('Year', validators=[Optional()])
    language = SelectField('Language', choices=languages, validators=[Optional()])
    extension = SelectField('Extension', choices=extensions, validators=[Optional()])
    submit = SubmitField('Find')

class TitleSearchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = IntegerField('Year', validators=[Optional()])
    language = SelectField('Language', choices=languages, validators=[Optional()])
    extension = SelectField('Extension', choices=extensions, validators=[Optional()])
    submit = SubmitField('Find')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')
