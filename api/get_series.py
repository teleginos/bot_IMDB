import requests

from config_data import config

key = config.RAPID_API_KEY
host = config.RAPID_API_HOST
url = config.URL_SERIES

headers = {
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": host
}

response = requests.get(url, headers=headers)


