from flask_sqlalchemy import SQLAlchemy
from pickle import FALSE
from flask import Flask
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(40), unique=True, nullable=False)
    author = db.Column(db.String(40), unique=False, nullable=False)
    publisher = db.Column(db.String(40), unique=False, nullable=True)

    def __repr__(self):
        return f"{self.book_name} - {self.description}"


@app.route('/')
def index():
    return "Hello!"


@app.route('/books')
def get_books():

    return {'book': 'book data'}
