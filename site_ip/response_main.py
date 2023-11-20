import requests
from loguru import logger

from site_ip.site_ip_handler import _make_response

BASE_URL = "http://makeup-api.herokuapp.com/api/v1/products.json?"

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

        with open('brand.txt', 'w+') as f:
            brands = []
            for item in _make_response():
                if item['brand'] is not None:
                    if item['brand'] not in brands:
                        brands.append(item['brand'])
            for items in brands:
                f.write('%s\n' % items)

        brand_handler()
        logger.info(f'Создан список брендов')


def product_type_handler() -> list:
    """

    :return: list
    """

    try:
        file = open('product_type.txt')
        product_types_list = sorted([line.strip() for line in file])
        file.close()
        return product_types_list
    except IOError:

        with open('product_type.txt', 'w+') as f:
            product_types = []
            for item in main_handler():
                if item['product_type'] is not None:
                    if item['brand'] not in product_types:
                        product_types.append(item['brand'])
            for items in product_types:
                f.write('%s\n' % items)
        product_type_handler()
        logger.info(f'Создан список типов')


def tag_handler() -> list:
    """

    :return: list: список тэгов.
    """
    try:
        file = open('tag.txt')
        tags_list = sorted([line.strip() for line in file])
        file.close()
        return tags_list
    except IOError:
        tags = []
        for item in main_handler():
            if item['tag_list']:
                for tag in item['tag_list']:
                    if tag not in tags:
                        tags.append(tag)
        with open('tag.txt', 'w+') as f:
            for items in tags:
                f.write('%s\n' % items)

        tag_handler()
        logger.info(f'Создан файл со всеми тэгами')


def name_handler(hand, cond):
    """

    :return: требуемое условие
    """

    for item in hand:
        if item[cond]:
            return item[cond]
        else:
            return "Ошибка"
