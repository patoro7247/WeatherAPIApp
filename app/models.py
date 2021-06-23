from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email= db.Column(db.String(120), index=True, unique=True)
	zip_code = db.Column(db.Integer, index=True)
	desired_temperature = db.Column(db.Integer, index=True)
	


	def __repr__(self):
		return '<User: {}>'.format(self.username)
