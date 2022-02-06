from simple_producer import simple_producer
from current_weather_provider import current_weather_provider
from sample_data import sample_weather_data
import yaml
import json
import requests
import time

in_conf_file = '../config/app_config.yaml'
out_conf_file = '../config/app_config.json'

with open(in_conf_file) as fpi:
    app_data = yaml.safe_load(fpi)
with open(out_conf_file, 'w') as fpo:
    json.dump(app_data, fpo, indent=2)

producer_conf = app_data['application']['kafka']['producer']['aiven']
providers_list = app_data['application']['data']['providers']

i=int(providers_list['current_weather_data']['call_count'])
while i > 0:
    dict = current_weather_provider()
    for key in dict:
        simple_producer(producer_conf, providers_list['current_weather_data']['topic_name'], key, dict[key])
    i -= 1

i=int(providers_list['sample_weather_data']['call_count'])
while i > 0:
    dict = sample_weather_data("../data/json/")
    for key in dict:
        simple_producer(producer_conf, providers_list['sample_weather_data']['topic_name'], key, dict[key])
    i -= 1

#end
