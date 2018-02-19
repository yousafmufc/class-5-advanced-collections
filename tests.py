from data import products_string
from step_1 import transform_products_to_list
from step_2 import group_products_by_customer
from step_3 import group_products_by_customer_and_invoice
from step_4 import calculate_total_per_invoices


def test_step_1_products_string_to_list():
    products_list = transform_products_to_list(products_string)
    assert type(products_list) == list
    assert len(products_list) == 50

    product_1 = products_list[0]
    assert product_1 == [
        '536365',
        '85123A',
        'WHITE HANGING HEART T-LIGHT HOLDER',
        '6',
        '12/1/10 08:26',
        '2.55',
        '17850',
        'United Kingdom']


def test_step_2_group_products_by_customer():
    products = group_products_by_customer(products_string)

    assert type(products) == dict
    assert len(products) == 4  # 4 customers

    customer_1 = products['17850']

    assert type(customer_1) == list
    assert len(customer_1) == 12

    customer_1[0] == [
        '536365',
        '85123A',
        'WHITE HANGING HEART T-LIGHT HOLDER',
        '6',
        '12/1/10 08:26',
        '2.55',
        '17850',
        'United Kingdom']
    assert customer_1[1] == [
        "536365",
        "71053",
        "WHITE METAL LANTERN",
        "6",
        "12/1/10 08:26",
        "3.39",
        "17850",
        "United Kingdom"
    ]

    customer_2 = products['13047']
    assert len(customer_2) == 17
    assert customer_2[0] == [
        "536367",
        "84879",
        "ASSORTED COLOUR BIRD ORNAMENT",
        "32",
        "12/1/10 08:34",
        "1.69",
        "13047",
        "United Kingdom"
    ]
    assert customer_2[-1] == [
        "536369",
        "21756",
        "BATH BUILDING BLOCK WORD",
        "3",
        "12/1/10 08:35",
        "5.95",
        "13047",
        "United Kingdom"
    ]


def test_step_3_group_by_customer_and_invoice():
    products = group_products_by_customer_and_invoice(products_string)
    assert type(products) == dict
    assert len(products) == 4  # 4 customers

    customer_1 = products['17850']

    assert type(customer_1) == dict
    assert len(customer_1) == 4

    # Invoice: 536365
    invoice = customer_1['536365']
    assert len(invoice) == 7
    assert invoice[0] == [
        "536365",
        "85123A",
        "WHITE HANGING HEART T-LIGHT HOLDER",
        "6",
        "12/1/10 08:26",
        "2.55",
        "17850",
        "United Kingdom"
    ]
    assert invoice[-1] == [
        "536365",
        "21730",
        "GLASS STAR FROSTED T-LIGHT HOLDER",
        "6",
        "12/1/10 08:26",
        "4.25",
        "17850",
        "United Kingdom"
    ]

    # Invoice: 536366
    invoice = customer_1['536366']
    assert len(invoice) == 2

    assert invoice[0] == [
        "536366",
        "22633",
        "HAND WARMER UNION JACK",
        "6",
        "12/1/10 08:28",
        "1.85",
        "17850",
        "United Kingdom"
    ]
    assert invoice[1] == [
        "536366",
        "22632",
        "HAND WARMER RED POLKA DOT",
        "6",
        "12/1/10 08:28",
        "1.85",
        "17850",
        "United Kingdom"
    ]

    # Invoice: 536372
    invoice = customer_1['536372']
    assert len(invoice) == 2

    assert invoice[0] == [
        "536372",
        "22632",
        "HAND WARMER RED POLKA DOT",
        "6",
        "12/1/10 09:01",
        "1.85",
        "17850",
        "United Kingdom"
    ]
    assert invoice[1] == [
        "536372",
        "22633",
        "HAND WARMER UNION JACK",
        "6",
        "12/1/10 09:01",
        "1.85",
        "17850",
        "United Kingdom"
    ]

    # Invoice: 536373
    invoice = customer_1['536373']
    assert len(invoice) == 1

    assert invoice[0] == [
        "536373",
        "85123A",
        "WHITE HANGING HEART T-LIGHT HOLDER",
        "6",
        "12/1/10 09:02",
        "2.55",
        "17850",
        "United Kingdom"
    ]


def test_step_4_calculate_totals():
    products = calculate_total_per_invoices(products_string)

    assert products == {
        '17850': {
            '536365': 139.12,
            '536366': 22.20,
            '536372': 22.20,
            '536373': 15.30,
        },
        '13047': {
            '536367': 278.73,
            '536368': 70.05,
            '536369': 17.85,
        },
        '12583': {
            '536370': 855.86
        },
        '13748': {
            '536371': 204
        }
    }
