from django.db import models


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Brand(BaseModel):
    title = models.CharField(max_length=64, verbose_name='عنوان')


class Item(BaseModel):
    sku = models.CharField(max_length=10, verbose_name='کد کالا', null=True, blank=True, unique=True)
    part_number = models.CharField(max_length=350, verbose_name='پارت نامبر', unique=True)
    brand = models.ForeignKey(Brand, related_name="items", verbose_name='برند', null=True, blank=True
                              , on_delete=models.DO_NOTHING)
    quality = models.CharField(max_length=100, verbose_name='کیفیت', null=True, blank=True)
    price = models.FloatField(verbose_name='قیمت')


class Customer(BaseModel):
    name = models.CharField(verbose_name='نام', max_length=200)
    national_id = models.CharField(verbose_name='کد ملی', max_length=10)


class Quotation(BaseModel):
    SALE_TYPE = ((1, 'نقدی'), (2, 'یک ماهه'), (3, 'سه ماهه'))
    customer = models.ForeignKey(Customer, verbose_name='مشتری', on_delete=models.DO_NOTHING)
    request_date = models.DateField(null=False, blank=False, verbose_name='تاریخ درخواست')
    cancel = models.BooleanField(default=False, verbose_name='کنسل')
    sale_type = models.PositiveSmallIntegerField(verbose_name='نوع فروش', choices=SALE_TYPE)


class QuotationItem(BaseModel):
    quotation = models.ForeignKey(Quotation, on_delete=models.DO_NOTHING, related_name='quotation_item_rel',
                                  verbose_name='پیش فاکتور')
    quantity = models.BigIntegerField(verbose_name="تعداد")
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, related_name='item_set')
    discount_per_item = models.FloatField('تخفیف هر ردیف', default=0)
