from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, InputRequired
from wtforms.fields.html5 import EmailField
class PostForm(FlaskForm):
	city = StringField('City', validators = [InputRequired(message="City required")])
	state = StringField('State', validators = [InputRequired(message="State required")])
	temp = IntegerField('Temp', validators = [InputRequired(message="Temperature required")])
	humidity = IntegerField('Humidity', validators = [InputRequired(message="Humidity required")])
	email = EmailField('Email', validators = [InputRequired(message="Email required")])
	submit = SubmitField('Submit')
	
	ReceiveNotifications = BooleanField('Recieve Post Notifications')


