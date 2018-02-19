from step_1 import transform_products_to_list


def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)

    products = {}
    for product in products_list:
        invoice_id = product[0]
        customer_id = product[-2]
        price = float(product[-3])
        quantity = float(product[-5])

        products.setdefault(customer_id, {})
        products[customer_id].setdefault(invoice_id, 0)
        products[customer_id][invoice_id] += round(quantity * price, 3)

    return products
