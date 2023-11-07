import requests
from loguru import logger


def main_handler():
    base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
    response = requests.get(base_url)
    data = response.json()
    return data


def brand_handler() -> list:
    """

    :return:
    """
    try:
        file = open('brand.txt')
        brands_list = sorted([line.strip() for line in file])
        file.close()
        return brands_list

    except IOError:
        brands = []
        for item in main_handler():
            print(item)
            if item['brand'] is not None:
                if item['brand'] not in brands:
                    brands.append(item['brand'])
        with open('brand.txt', 'w+') as f:
            for items in brands:
                f.write('%s\n' % items)

        brand_handler()
        logger.info(f'Создан список брендов')


def product_types_handler():
    try:
        file = open('product_type.txt')
        product_types_list = sorted([line.strip() for line in file])
        file.close()
        return product_types_list
    except IOError:
        product_types = []
        for item in main_handler():
            if item['product_type'] is not None:
                if item['product_type'] not in product_types:
                    product_types.append(item['product_type'])
        with open('product_type.txt', 'w+') as f:
            for items in product_types:
                f.write('%s\n' % items)
        product_types_handler()
        logger.info(f'Создан список типов')


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
