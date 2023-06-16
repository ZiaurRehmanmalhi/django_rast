import requests
import json

URL = ""


def get_data(id = None):
    if id is not None:
        data = {'id': id}

