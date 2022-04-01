from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField,TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name:")
    species = SelectField("Species:",
        choices = [("dog","Dog"),("cat","Cat"),("porcupine","Porcupine")])
    photo_url = StringField("Photo URL:",
        validators=[Optional(),URL()])
    age = SelectField("Age",
        choices=[("baby", "Baby"), ("young", "Young"), ("adult", "Adult"), ("senior", "Senior")]
        )
    notes = TextAreaField("Enter Any Notes:")

class EditPetForm(FlaskForm):
    """Form for edit pets info."""

    photo_url = StringField("Photo URL:",
        validators=[Optional(),URL()])
    notes = TextAreaField("Enter Any Notes:")
    available = BooleanField("Available?")
