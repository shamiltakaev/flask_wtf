from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    userId = StringField("ID астронавта", validators=[DataRequired()])
    password_1 = PasswordField("Пароль астронавта", validators=[DataRequired()])
    capitanID = StringField("ID астронавта", validators=[DataRequired()])
    password_2 = PasswordField("Пароль астронавта", validators=[DataRequired()])
    submit = SubmitField("Доступ")
    
