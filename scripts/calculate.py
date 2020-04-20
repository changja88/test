from datetime import datetime

from margin.models import Margin
from purchase.models import Purchase
from sales.models import Sales

standard_date = datetime(year=2020, month=4, day=20)


def run():
    sales = Sales.objects.filter(standard_date=standard_date).order_by('order_number')

    agregated_sale = []
    for index, sale in enumerate(sales):
        if len(agregated_sale) == 0:
            agregated_sale.append(sale)
        else:
            if sale.order_number == agregated_sale[0].order_number:
                agregated_sale.append(sale)
            else:
                calcualate(agregated_sale)
                agregated_sale.clear()
                agregated_sale.append(sale)

        if len(sales)== index+1:
            calcualate(agregated_sale)

def calcualate(agregated_sale):
    hitomi_price = get_hitomi_price(agregated_sale[0].order_number)
    amount_of_payment = get_amout_of_payment(agregated_sale)
    payment_fee = abs(get_payment_fee(agregated_sale))
    connection_fee = abs(get_connection_fee(agregated_sale))

    Margin.objects.create(
        standard_date = standard_date,
        hitomi_price=hitomi_price,
        customer_name=agregated_sale[0].customer_name,
        order_number=agregated_sale[0].order_number,
        amount_of_payment=amount_of_payment,
        payment_fee=payment_fee,
        connection_fee=connection_fee,
        margin=amount_of_payment -payment_fee -connection_fee - hitomi_price
    )


def get_hitomi_price(order_number):
    hitomi_prices = Purchase.objects.filter(order_number=order_number).values_list('hitomi_price', flat=True)
    hitomi_price = 0
    for price in hitomi_prices:
        hitomi_price += price
    return hitomi_price


def get_amout_of_payment(agregated_sale):
    amout_of_payment = 0
    for one_sale in agregated_sale:
        amout_of_payment += one_sale.amount_of_payment
    return amout_of_payment


def get_payment_fee(agregated_sale):
    payment_fee = 0
    for one_sale in agregated_sale:
        payment_fee += one_sale.payment_fee
    return payment_fee


def get_connection_fee(agregated_sale):
    connection_fee = 0
    for one_sale in agregated_sale:
        connection_fee += one_sale.connection_fee
    return connection_fee
