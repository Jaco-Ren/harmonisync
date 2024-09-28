from wtforms import (
    BooleanField,
    StringField,
    PasswordField,
    SubmitField,
    FileField,
)
from wtforms.validators import DataRequired, Email, Length, InputRequired, EqualTo
from flask_wtf import FlaskForm


# Classes to handle forms


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[Length(4, 25), DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(5, 30)])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            Length(5, 30),
            EqualTo("password"),
        ],
    )
    is_creator = BooleanField("Are you a creator?")
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(5, 30)])
    submit = SubmitField("Login")


class MusicFilesForm(FlaskForm):
    title = StringField("Nickname", validators=[DataRequired(), Length(1, 20)])
    music_file = FileField("Music File", validators=[DataRequired()])
    submit = SubmitField("Send")
