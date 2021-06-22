import requests

from datetime import datetime

api_key = '7d4535df12dc7fe25379fe942c3b6eb4'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("\n-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

f = open("weather.txt", 'w+')
f.write('''\n-------------------------------------------------------------\nWeather Stats for - {}  || {}'''.format(location.upper(), date_time)+
        '''\n-------------------------------------------------------------\n\nCurrent temperature is :  {:.2f} deg C'''.format(temp_city)+
        '''\nCurrent weather desc   :  '''+weather_desc+
        '''\nCurrent Humidity       :  '''+str(hmdt)+ '%' +
        '''\nCurrent wind speed     :  '''+str(wind_spd) +'kmph')

f.close()

print("\nData added to file ")
