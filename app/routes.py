from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import PostForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = PostForm()
	if form.validate_on_submit():
		flash('Submission Requested for:\nCity: {}, State: {}'.format(form.city.data, form.state.data))
		return redirect(url_for('confirmation'))
	return render_template('index.html', form=form)

@app.route('/confirmation')
def confirmation():
	return 'Thank you for submitting'

