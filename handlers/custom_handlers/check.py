def check_cond_in_file(condition, name) -> bool:
    """
    Происходит проверка наличия введенного условия

    :param name: введеное название
    :param condition: выбранное условие
    :return: bool
    """

    if condition == "brand":
        with open('brand.txt') as f:
            if name in f.read():
                return True
            else:
                return False

    elif condition == "tag":
        with open('tag.txt') as f:
            if name in f.read():
                return True
            else:
                return False

    if condition == "product_type":
        with open('product_type.txt') as f:
            if name in f.read():
                return True
            else:
                return False
