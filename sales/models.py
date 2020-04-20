from django.db import models


class Sales(models.Model):
    standard_date = models.DateField(blank=False, null=False, db_index=True, help_text='정산일')
    order_number = models.TextField(blank=False, null=False, db_index=True, help_text='주문번호')
    product_number = models.TextField(blank=False, null=False, help_text='상품 주문번호')
    product_name = models.TextField(blank=False, null=False, db_index=True, help_text='상품명')

    category = models.TextField(blank=False, null=False, help_text='배송비/상품주문')
    customer_name = models.TextField(blank=False, null=False, help_text='구매자명')
    amount_of_payment = models.IntegerField(blank=False, null=False, help_text='결제금액')
    payment_fee = models.IntegerField(blank=False, null=False, help_text='결제수수료')
    connection_fee = models.IntegerField(blank=False, null=False, help_text='연동수수료')

    class Meta:
        db_table = 'sales'
        verbose_name = 'sales - 정산내역'
        verbose_name_plural = 'sales - 정산내역'
        unique_together = (
            ('standard_date', 'order_number', 'product_number', 'product_name')
        )


    def __str__(self):
        return f'order_number : {self.order_number}, customer_name : {self.customer_name} amount_of_payment : {self.amount_of_payment}'
