from step_1 import transform_products_to_list


def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)

    products = {}
    for product in products_list:
        invoice = product[0]
        customer_id = product[-2]

        products.setdefault(customer_id, {})

        products[customer_id].setdefault(invoice, [])
        products[customer_id][invoice].append(product)

    return products
