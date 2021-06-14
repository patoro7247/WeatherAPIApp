from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
class PostForm(FlaskForm):
	city = StringField('City', validators = [DataRequired()])
	state = StringField('State', validators = [DataRequired()])
	temp = IntegerField('Temp', validators = [DataRequired()])
	humidity = IntegerField('Humidity', validators = [DataRequired()])
	email = EmailField('Email', validators = [DataRequired()] )
	submit = SubmitField('Submit')
	
	ReceiveNotifications = BooleanField('Recieve Post Notifications')


