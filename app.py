from flask import Flask, render_template, request
from forms import SignUpForm
import os

app = Flask(__name__)
app.config["SECRET KEY"] = "secret"

posts = [
    {"character": "Arthurius",
     "power": "Telepathy",
     "weapon": "Sword",
     "description": "Really smart but grades are pretty low, which is surprising because he should be able to read his professors' minds during a test. Maybe he chooses not to. He's also super friendly and kind."},

    {"character": "Fantasia",
     "power": "Telekinesis",
     "weapon": "Sword",
     "description": "Shy and likes to play with talking raccoons"},

    {"character": "Obsidian",
     "power": "Invisibility",
     "weapon": "Spear",
     "description": "No one knows for sure who Obsidian really is. This boy just popped our of nowhere one day. Many people suspect that he's always been around, silently starting at everyone."}
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/characters')
def character():
    return render_template('character.html', posts=posts, title="Characters")

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)
