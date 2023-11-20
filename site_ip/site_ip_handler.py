from typing import Dict

import requests

BASE_URL = "http://makeup-api.herokuapp.com/"
params = {"brand", "name", "tag_list"}
response = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json")

print(response.params)


def main_handler(url):
    response = requests.get(url)
    data = response.json()
    return data


def _make_response(params: Dict, timeout: int, success=200):
    response = requests.request(
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code

