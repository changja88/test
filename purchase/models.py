from django.db import models


class Purchase(models.Model):
    upload_date = models.DateField(blank=False, null=False, help_text='업로드 날짜')
    order_number = models.BigIntegerField(blank=False, null=False, db_index=True, help_text='주문번호')
    customer_name = models.TextField(blank=False, null=False, help_text='구매자명')
    count = models.IntegerField(blank=False, null=False, help_text='구매 갯수')
    receiver_name = models.TextField(blank=False, null=False, help_text='수취인 명')
    hitomi_price = models.IntegerField(blank=False, null=False, help_text='히토미 가')

    class Meta:
        db_table = 'purchase'
        verbose_name = 'purchase - 구매내역'
        verbose_name_plural = 'purchase - 구매내역'
