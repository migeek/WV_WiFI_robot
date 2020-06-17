from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign up')

    # def validate_<fieldname>() adds to stock validators for additional validation
    def validate_username(self, username):
        user_query = User.query.filter_by(username=username.data).first()
        if user_query is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        email_query = User.query.filter_by(email=email.data).first()
        if email_query is not None:
            raise ValidationError('Please use a different email')



class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remeber Me')
    submit=SubmitField('Login')

