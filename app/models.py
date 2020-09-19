#first, last, dob, county, phone, email

from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first = db.Column(db.String(1))
	last = db.Column(db.String(50))
	dob = db.Column(db.Integer)
	phone = db.Column(db.Integer)
	email = db.Column(db.String(50))
