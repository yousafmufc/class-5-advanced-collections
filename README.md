# Class 5: Advanced collections practice

**[Spreadsheet with data](https://docs.google.com/spreadsheets/d/1WxvM9V_rgHlKLhQ7SEz6J7P0t6Nh9oF7-fBr9EZylGs/edit?usp=sharing)**

### Step 1: String to List

The first step is to parse the raw string into a list containing products (as lists). It'll end up being a nested collections (a list of lists).

### Step 2: Group by customers

Group invoices per customer. Your final result will look something like:

```python
{
    '17850': [  # Customer ID
        [
            '536365',
            '85123A',
            'WHITE HANGING HEART T-LIGHT HOLDER',
            '6',
            '12/1/10 08:26',
            '2.55',
            '17850',
            'United Kingdom'
        ],
        [
            "536365",
            "71053",
            "WHITE METAL LANTERN",
            "6",
            "12/1/10 08:26",
            "3.39",
            "17850",
            "United Kingdom"
        ]
    ]
}
```


### Step 3: Group by customers and invoice number

Group invoices by customer and invoice number. Your final result will look something like:

```python
{
    '17850': {  # Customer ID
        '536365': [  # Invoice ID
            [
                "536365",
                "85123A",
                "WHITE HANGING HEART T-LIGHT HOLDER",
                "6",
                "12/1/10 08:26",
                "2.55",
                "17850",
                "United Kingdom"
            ],
            ...
            [
                "536365",
                "21730",
                "GLASS STAR FROSTED T-LIGHT HOLDER",
                "6",
                "12/1/10 08:26",
                "4.25",
                "17850",
                "United Kingdom"
            ]
        ],
        '536366': [  # Invoice ID
            [
                "536366",
                "22633",
                "HAND WARMER UNION JACK",
                "6",
                "12/1/10 08:28",
                "1.85",
                "17850",
                "United Kingdom"
            ],
            [
                "536366",
                "22632",
                "HAND WARMER RED POLKA DOT",
                "6",
                "12/1/10 08:28",
                "1.85",
                "17850",
                "United Kingdom"
            ]
        ]
    }
}
```

### Step 4: Calculate total per invoice per customer

Calculate each invoice's total and keep them also grouped by customer.

![image](https://user-images.githubusercontent.com/872296/36392376-b3ff802a-1589-11e8-887e-43c9b6faf80d.png)

Expected result will look:

```python
{
    '17850': {  # Customer ID
        '536365': 139.12,  # Total for Invoice ID #536365
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
```
