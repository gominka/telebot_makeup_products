import requests


def main_handler():
    base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
    response = requests.get(base_url)
    data = response.json()
    return data


def brand_handler():
    brands = []
    for item in main_handler():
        if item['brand'] is not None:
            if item['brand'] not in brands:
                brands.append(item['brand'])
    with open('brand.txt', 'w+') as f:
        for items in brands:
            f.write('%s\n' % items)


def types_handler():
    product_types = []
    for item in main_handler():
        if item['product_type'] is not None:
            if item['product_type'] not in product_types:
                product_types.append(item['product_type'])
    with open('product_type.txt', 'w+') as f:
        for items in product_types:
            f.write('%s\n' % items)


def tag_handler():
    tags = []
    for item in main_handler():
        if item['tag_list']:
            for tag in item['tag_list']:
                if tag not in tags:
                    tags.append(tag)
    with open('tag.txt', 'w+') as f:
        for items in tags:
            f.write('%s\n' % items)
