from datetime import datetime

import numpy

from purchase.models import Purchase

purchase_info_file = '2020-04-19.csv'  # 파일이름일자 까지의 발주 정보
upload_date = datetime(year=2020, month=4, day=19)

order_number_index = 0
customer_index = 1
count_index = 2
receiver_name_index = 3
hitomi_price_index = 4


def run():
    purchase_info = numpy.loadtxt(f'data/purchase/{purchase_info_file}', delimiter=',', dtype=numpy.str, skiprows=2)

    for purchase in purchase_info:
        Purchase.objects.create(
            upload_date=upload_date,
            order_number=purchase[order_number_index],
            customer_name=purchase[customer_index],
            count=purchase[count_index],
            receiver_name=purchase[receiver_name_index],
            hitomi_price=purchase[hitomi_price_index]
        )
