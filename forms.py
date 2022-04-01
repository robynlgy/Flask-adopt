from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField,TextAreaField


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name:")
    species = StringField("Species:")
    photo_url = StringField("Photo URL:")
    age = SelectField("Age",
        choices=[("baby", "Baby"), ("young", "Young"), ("adult", "Adult"), ("senior", "Senior")]
        )
    notes = TextAreaField("Enter Any Notes:")  