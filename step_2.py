from step_1 import transform_products_to_list
from data import products_string

def group_products_by_customer(products_string):
    products_list = transform_products_to_list(products_string)

    customers = {}

    for product in products_list:
        customer_id = product[-2]

        customers.setdefault(customer_id,[])

        customers[customer_id].append(product)



    return customers