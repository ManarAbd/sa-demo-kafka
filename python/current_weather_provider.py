import yaml
import json
import requests
import time

service_conf_file = '../config/service_config.yaml'

def current_weather_provider():
    dict = {}
    with open(service_conf_file) as fps:
        service_data = yaml.safe_load(fps)

    service_url = service_data['service']['openweathermap']['current_weather_data']['url']
    cities = service_data['service']['openweathermap']['current_weather_data']['cities']
    appid = service_data['service']['openweathermap']['current_weather_data']['appid']
    units = service_data['service']['openweathermap']['current_weather_data']['units']


    for city in cities:
        req = service_url + "weather?q=" + city + "&appid=" + appid + "&units=" + units
        response = requests.get(req)
        print (req)
        key = city
        dict[key] = response.json()
        time.sleep(1)

    print ('#')
    print (dict)
    print ('#')   
    return dict
