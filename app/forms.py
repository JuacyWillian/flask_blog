from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    publish = BooleanField('Publish?')

    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    username = StringField('Username:', [DataRequired(), Length(min=6)])
    password = PasswordField('Password:', [DataRequired(), Length(min=6)])
    remember = BooleanField('Remember me!')

    submit = SubmitField('Submit')


class RegisterForm(LoginForm):
    email = StringField('Email Address:', [DataRequired(), Email()])


class PasswordResetForm(FlaskForm):
    pass


class PasswordRecoveryForm(FlaskForm):
    pass
