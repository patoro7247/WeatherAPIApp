#iterate through users in db, get the daily high for their zip code, #compare it to their desired temp, if it is at or above desired temp, #send an email

import json
import requests
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from app import db
from app.models import User

load_dotenv('.env')

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
OPEN_WEATHER_KEY = os.environ.get('API_KEY')


#email stuff
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()

	#encrypt traffic
	smtp.starttls()
	smtp.ehlo()

	#log in to mail server
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

	#make subject, body, and msg
	msg = EmailMessage()
	msg['Subject'] = 'It\'s going to be nice out today!'
	msg['From'] = EMAIL_ADDRESS
	


	users = User.query.all()

	for u in users:
		a_username = u.username 
		split_username = a_username.split('@',1)
		a_username = split_username[0]


		call = 'https://api.openweathermap.org/data/2.5/forecast/daily?zip={}&cnt=1&appid={}&units=imperial'.format(u.zip_code, OPEN_WEATHER_KEY)

		response = requests.get(call).json()

		forecasted_temperature = response["list"][0]['temp']['max']

		if forecasted_temperature >= u.desired_temperature:
			print("The forecasted temperature for {} is {}, which is greater than {}'s desired temperature of {}.".format(u.zip_code, forecasted_temperature, u.username, u.desired_temperature))

			#make subject, body, and msg
			msg['To'] = u.email 
			print(type(u.email))
			msg.set_content(f'Hello {a_username}, it\'s going to be {forecasted_temperature} degrees outside today, which is higher than your desired temperature of {u.desired_temperature}')

			#sendmail(Sender, Receiver, msg)
			smtp.send_message(msg)

		else:
			print("The forecasted temperature for {} is {}, which is less than {}'s desired temperature of {}.".format(u.zip_code, forecasted_temperature, u.username, u.desired_temperature))

			msg['To'] = u.email 
			print(type(u.email))
			msg.set_content(f'Hello {a_username}, it\'s going to be {forecasted_temperature} degrees outside today, which is lower than your desired temperature of {u.desired_temperature}')

			#sendmail(Sender, Receiver, msg)
			smtp.send_message(msg)

