# Import SQLAlchemy#

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

# Set the config variable to the database file
app.config['SQLALCHEMY_DATABASE_URI'] =\
  'sqlite:///' + os.path.join(basedir, 'database.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection#
db = SQLAlchemy(app)

# Model
# class Post(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(100), nullable=False, unique=False)
#   desc = db.Column(db.String(200), nullable=False)
#   img_url = db.Column()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(), nullable=False, unique=True)
  password = db.Column(db.String(50), nullable=False, unique=True)

# db.create_all()
def __repr__(self):
  return f'<Student {self.email}>'

class Employee(db.Model):
  employee_id = db.Column(db.Integer, primary_key=True, nullable=False)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  
  # this column will be added inside the Employee model because an employee is only associated with one Department instance.
  department_name = db.Column(db.String(50), db.ForeignKey('department.name'), nullable=False)

class Department(db.Model):
  name = db.Column(db.String(50), primary_key=True, nullable=False) 
  location = db.Column(db.String(50), nullable=False)
  employees = db.relationship('Employee', backref='department')
  
class Project(db.Model):
  project_id = db.Column(db.Integer, primary_key=True, nullable=False)
  name = db.Column(db.String(50), nullable=False)

# Adding relationships
