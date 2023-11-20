from loguru import logger
from site_ip.site_ip_handler import _make_response


def cond_handler(msg_user) -> list:
    """
    :return:
    """

    if msg_user == "brand":
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

            logger.info(f'Создан список брендов')
            return cond_handler("brand")

    elif msg_user == "product_type":
        try:
            file = open('product_type.txt')
            product_types_list = sorted([line.strip() for line in file])
            file.close()
            return product_types_list
        except IOError:
            with open('product_type.txt', 'w+') as f:
                product_types = []
                for item in _make_response():
                    if item['product_type'] is not None:
                        if item['product_type'] not in product_types:
                            product_types.append(item['product_type'])
                for items in product_types:
                    f.write('%s\n' % items)
            logger.info(f'Создан список типов')
            return cond_handler("product_type")

    elif msg_user == "tag":
        try:
            file = open('tag.txt')
            tags_list = sorted([line.strip() for line in file])
            file.close()
            return tags_list
        except IOError:
            tags = []
            for item in _make_response():
                if item['tag_list']:
                    for tag in item['tag_list']:
                        if tag not in tags:
                            tags.append(tag)
            with open('tag.txt', 'w+') as f:
                for items in tags:
                    f.write('%s\n' % items)

            logger.info(f'Создан файл со всеми тэгами')
            return cond_handler("tag")
