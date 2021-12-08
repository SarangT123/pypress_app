from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from website.models import User


class Register(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=3, max=20)], render_kw={'placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={'placeholder': 'Password'})
    submit = SubmitField("Register")

    def validate_username(self, username):
        exist = User.query.filter_by(username=username.data).first()

        if exist:
            raise ValidationError("Username taken")


class Login(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=3, max=20)], render_kw={'placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={'placeholder': 'Password'})
    submit = SubmitField("Login")
