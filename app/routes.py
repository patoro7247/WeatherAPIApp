from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import User
from app.forms import RegistrationForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = RegistrationForm()
	if form.validate_on_submit():
		#user = User.query.filter_by(username=form.email.data).first()
		location = form.city.data + ', '+form.state.data

		user = User(username=form.username.data, address=location, desired_temperature=form.temp.data)
		db.session.add(user)
		db.session.commit()
		flash('We\'ll now send you an email whenever the temperature high in your city is at or above your desired temp')
		return redirect(url_for('confirmation'))
	return render_template('index.html', form=form)

@app.route('/confirmation')
def confirmation():
	return 'Thank you for submitting'

