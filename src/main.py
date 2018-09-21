import json
import bs4
import requests

def is_id_channel(id):
    url = f'https://www.youtube.com/channel/{id}'
    req = requests.get(url)
    return req.status_code is 200

