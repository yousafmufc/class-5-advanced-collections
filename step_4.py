from step_1 import transform_products_to_list
from data import products_string

def calculate_total_per_invoices(products_string):

    products_list = transform_products_to_list(products_string)

    products = {}

    for product in products_list:

        customer_id = product[-2]
        invoice_id = product[0]
        item_price = float(product[-3])
        quantity = int(product[3])

        products.setdefault(customer_id,{})

        products[customer_id].setdefault(invoice_id,0)

        products[customer_id][invoice_id] += round(item_price*quantity,2)

    return products


