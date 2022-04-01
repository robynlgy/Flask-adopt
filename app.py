"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, request, flash

from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm

from models import db, connect_db, Pet


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

@app.get('/')
def get_homepage():
    """Shows homepage with list of pets"""

    pets = Pet.query.all()

    return render_template("index.html", pets = pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}!")
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)
