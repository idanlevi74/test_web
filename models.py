import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Company(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  company_id = db.Column(db.String(30))
  company_name = db.Column(db.String(30))
  docs = db.relationship('Docs')


class Docs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String(30))
  file = db.Column(db.String(30))
  id = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  company_id = db.Column(db.Integer, db.ForeignKey('company.id'))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(30))
  first_name = db.Column(db.String(30))
  last_name = db.Column(db.String(30))
  phone_number = db.Column(db.String(10), unique=True)
  docs = db.relationship('Docs')
