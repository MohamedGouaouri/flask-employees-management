from app import db
from datetime import datetime


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    employed_at = db.Column(db.DateTime, default=datetime.utcnow)
    country = db.Column(db.String(10), nullable=False)
    hours_per_day = db.Column(db.Intger, nullable=False)
    salary = db.Column(db.Intger, nullable=False)
    role =  db.relationship('Role', backref='code', lazy='dynamic')
    current_project =  db.relationship('Project', backref='name', lazy='dynamic')


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), index=True, nullable=False)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    started_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    deadline = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
