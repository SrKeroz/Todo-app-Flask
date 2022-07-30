from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("send")


class TodoForm(FlaskForm):
    description = StringField("Descipcion", validators=[DataRequired()])
    sumit = SubmitField("create")


class DeleteTodo(FlaskForm):
    submit = SubmitField("Delete")

class UpdateTodo(FlaskForm):
    submit = SubmitField("update")