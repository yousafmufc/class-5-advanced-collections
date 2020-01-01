from data import products_string


def transform_products_to_list(products_string):


    data_list = products_string.split("\n")
    products_list = []

    for data in data_list:
        if data == "":
            continue
        product = data.split(',')
        products_list.append(product)

    return products_list