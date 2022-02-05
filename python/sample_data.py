import yaml
import json
import requests
import time
import os

def sample_weather_data(data_files):
    dict = {}

    for filename in os.listdir(data_files):
        with open(os.path.join(data_files, filename), 'r') as f:
            text = f.read()
            key = filename
            dict[key] = text
            time.sleep(1)

    print ('#')
    print (dict)
    print ('#')   
    return dict
