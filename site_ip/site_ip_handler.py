from typing import Dict

import requests

BASE_URL = "http://makeup-api.herokuapp.com/api/v1/products.json"
params_dict = {"product_type": None,
               "product_category": None,
               "product_tags": None,
               "brand": None,
               "price_greater_than": None,
               "price_less_than": None,
               "rating_greater_than": None,
               "rating_less_than": None,
               }


def _make_response(params: Dict = params_dict, success=200):
    response = requests.get(
        url=BASE_URL,
        params=params,
    )
    print(response.url)
    status_code = response.status_code

    if status_code == success:
        return response.json()

    return status_code