from datetime import datetime

import numpy

from sales.models import Sales

order_number_index = 0
product_number_index = 1
category_index = 2
product_name_index = 3
customer_name_index = 4
amount_of_payment_index = 8
payment_fee_index = 9
connection_fee_index = 10

today = datetime(year=2020, month=4, day=20)
daily_sale_file = '2020-04-20.csv'


def run():
    daily_sale = numpy.loadtxt(f'data/sale/{daily_sale_file}', delimiter=',', dtype=numpy.str, skiprows=1)
    for order in daily_sale:
        Sales.objects.create(
            standard_date=today,
            order_number=order[order_number_index],
            product_number=order[product_number_index],
            product_name=order[product_name_index],
            category=order[category_index],
            customer_name=order[customer_name_index],
            amount_of_payment=order[amount_of_payment_index],
            payment_fee=order[payment_fee_index],
            connection_fee=order[connection_fee_index]
        )
