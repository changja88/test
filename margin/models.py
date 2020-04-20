from django.db import models


# Create your models here.


class Margin(models.Model):
    standard_date = models.DateField(blank=False, null=False, db_index=True, help_text='정산일')
    customer_name = models.TextField(blank=False, null=False, help_text='구매자명')
    order_number = models.BigIntegerField(blank=False, null=False, db_index=True, help_text='주문번호', unique=True)
    hitomi_price = models.IntegerField(blank=False, null=False, help_text='히토미 가')
    amount_of_payment = models.IntegerField(blank=False, null=False, help_text='결제금액')
    payment_fee = models.IntegerField(blank=False, null=False, help_text='결제수수료')
    connection_fee = models.IntegerField(blank=False, null=False, help_text='연동수수료')

    margin = models.IntegerField(blank=False, null=False, help_text='마진')

    class Meta:
        db_table = 'margin'
        verbose_name = 'magin - 마진 내역'
        verbose_name_plural = 'magin - 마진 내역'
