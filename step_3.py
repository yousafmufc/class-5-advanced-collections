from step_1 import transform_products_to_list
from data import products_string

def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)

    products = {}

    for product in products_list:

        customer_id = product[-2]
        invoice_id = product[0]
        products.setdefault(customer_id,{})

        products[customer_id].setdefault(invoice_id,[])

        products[customer_id][invoice_id].append(product)


    return products
