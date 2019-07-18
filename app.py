import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#__file__ is set to the file you are working on
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET KEY'] = "mykey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Puppy(db.Model):
  __tablename__ = 'puppies'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  age = db.Column(db.Integer)

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Puppy {self.name} is {self.age}"


# if __name__ == '__main__':
#   app.run(debug=True)
