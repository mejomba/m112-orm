# Generated by Django 4.2.3 on 2024-08-19 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_brand_delete_date_remove_brand_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationitem',
            name='price',
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=64, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='national_id',
            field=models.CharField(max_length=10, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='core.brand', verbose_name='برند'),
        ),
        migrations.AlterField(
            model_name='item',
            name='part_number',
            field=models.CharField(max_length=350, unique=True, verbose_name='پارت نامبر'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quality',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='کیفیت'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='کد کالا'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='cancel',
            field=models.BooleanField(default=False, verbose_name='کنسل'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.customer', verbose_name='مشتری'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='request_date',
            field=models.DateField(verbose_name='تاریخ درخواست'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='sale_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'نقدی'), (2, 'یک ماهه'), (3, 'سه ماهه')], verbose_name='نوع فروش'),
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='discount_per_item',
            field=models.FloatField(default=0, verbose_name='تخفیف هر ردیف'),
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='quantity',
            field=models.BigIntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='quotation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='quotation_item_rel', to='core.quotation', verbose_name='پیش فاکتور'),
        ),
    ]