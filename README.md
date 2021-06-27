# Weather API App

This web app takes a user's location, desired temperature, email address, which is then entered into a database(sqlite).
I'm using OpenWeatherMap's API that takes each user's zip code in the database to get the forecasted high temperature for that day.  
If the forecasted high temperature for that day is equal to or greater the user's desired_temperature, the user will be sent an email
using python's smtplib that will notify them.  
