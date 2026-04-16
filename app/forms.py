from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    poster = FileField(
        "Poster",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "jpeg", "png"], "Images only!"),
        ],
    )
