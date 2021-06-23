#iterate through users in db, get the daily high for their zip code, #compare it to their desired temp, if it is at or above desired temp, #send an email

import json
import requests
from app import db
from app.models import User
from secret import open_weather_key


#print(response["list"][0]['temp']['max'])


users = User.query.all()

for u in users:
	call = 'https://api.openweathermap.org/data/2.5/forecast/daily?zip={}&cnt=1&appid={}&units=imperial'.format(u.zip_code, open_weather_key)

	response = requests.get(call).json()

	forecasted_temperature = response["list"][0]['temp']['max']

	if forecasted_temperature >= u.desired_temperature:
		print("The forecasted temperature for {} is {}, which is greater than {}'s desired temperature of {}.".format(u.zip_code, forecasted_temperature, u.username, u.desired_temperature))
	else:
		print("The forecasted temperature for {} is {}, which is less than {}'s desired temperature of {}.".format(u.zip_code, forecasted_temperature, u.username, u.desired_temperature))



