from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileAllowed
from werkzeug.datastructures import FileStorage


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    photo = FileField ("Upload Image", validators=[DataRequired(), FileAllowed(['jpg','png'])])
    
