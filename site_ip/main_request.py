import json
from typing import Dict, List

import requests

BASE_URL = "http://makeup-api.herokuapp.com/api/v1/products.json"
BASE_PARAMS = {
    "name": None,
    "product_type": None,
    "product_category": None,
    "product_tags": None,
    "brand": None,
    "price_greater_than": None,
    "price_less_than": None,
    "rating_greater_than": None,
    "rating_less_than": None
}


def make_response(params: Dict, success=200):
    response = requests.request("GET", BASE_URL, params=params, timeout=10)
    status_code = response.status_code

    if status_code == success:
        return json.loads(response.text)

    return status_code


def conditions_list(params: dict, selected_condition: str) -> List:
    """Making lists

    :param selected_condition: user's message
    :param params: selected parameters

    :return: list of possible conditions
    """

    data = make_response(params)

    if selected_condition == "brand":
        brands = sorted(list(set([item['brand'] for item in data if item['brand'] is not None])))
        return brands

    elif selected_condition == "product_tag":
        tags = sorted(list(set([tag for item in data for tag in item['tag_list'] if item['tag_list']])))
        return tags

    elif selected_condition == "product_type":
        product_types = sorted(list(set([item['product_type'] for item in data if item['product_type'] is not None])))
        return product_types

    elif selected_condition == "list_name_product":
        name_product = sorted(list(set([item['name'] for item in data if item['name'] is not None])))
        return name_product

    elif selected_condition == "all_condition":
        brands = sorted(list(set([item['brand'] for item in data if item['brand'] is not None])))
        tags = sorted(list(set([tag for item in data for tag in item['tag_list'] if item['tag_list']])))
        product_types = sorted(list(set([item['product_type'] for item in data if item['product_type'] is not None])))
        return brands + tags + product_types

