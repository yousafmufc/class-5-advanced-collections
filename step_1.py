def transform_products_to_list(products_string):
    split_products = products_string.split('\n')
    products_list = []

    for product_line in split_products:
        if product_line:
            product = product_line.split(',')
            products_list.append(product)
    return products_list
