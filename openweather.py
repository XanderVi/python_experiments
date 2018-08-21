import requests
from elasticsearch import Elasticsearch

#personal API key
api_key = "9a285bdbdb3ab902f23c0f311daf3b7a"

#working code
'''
city_1 = input('Enter city & country name in the format like: Odessa,UA: ')
city_2 = input('Enter city & country name in the format like: Odessa,UA: ')
city_3 = input('Enter city & country name in the format like: Odessa,UA: ')
city_4 = input('Enter city & country name in the format like: Odessa,UA: ')
city_5 = input('Enter city & country name in the format like: Odessa,UA: ')
city_6 = input('Enter city & country name in the format like: Odessa,UA: ')
city_7 = input('Enter city & country name in the format like: Odessa,UA: ')
city_8 = input('Enter city & country name in the format like: Odessa,UA: ')
city_9 = input('Enter city & country name in the format like: Odessa,UA: ')
city_10 = input('Enter city & country name in the format like: Odessa,UA: ')
'''

#test cities
city_1 = "Odessa,UA"
city_2 = "Kyiv,UA"
city_3 = "Mykolaiv,UA"
city_4 = "Lviv,UA"
city_5 = "Odessa,UA"
city_6 = "Kyiv,UA"
city_7 = "Mykolaiv,UA"
city_8 = "Lviv,UA"
city_9 = "Odessa,UA"
city_10 = "Kyiv,UA"

cities = [city_1, city_2, city_3, city_4, city_5,
          city_6, city_7, city_8, city_9, city_10]

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

try:
    res = requests.get('http://localhost:9200')
    for city in range(len(cities)):
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                params={'q': cities[city], 'type': 'like', 'units': 'metric', 'APPID': api_key})
        data = res.json()
        temp = data['list'][0]['main']['temp']
        temp_min = data['list'][0]['main']['temp_min']
        temp_max = data['list'][0]['main']['temp_max']
        humidity = data['list'][0]['main']['humidity']
        pressure = data['list'][0]['main']['pressure']
        wind_speed = data['list'][0]['wind']['speed']
        wind_degree = data['list'][0]['wind']['deg']
    
        weather = {'temp': temp, 'temp_min': temp_min, 'temp_max': temp_max, 'humidity': humidity,
                   'pressure': pressure, 'wind_speed': wind_speed, 'wind_degree': wind_degree}
        #'cw' means city weather
        es.index(index='cw', doc_type='weather', id=city, body=weather)

except Exception as e:
    print("Exception (find):", e)
