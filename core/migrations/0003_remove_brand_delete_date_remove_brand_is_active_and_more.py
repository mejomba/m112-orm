# Generated by Django 4.2.3 on 2024-08-18 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_itemweight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='is_spacial',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_spacial',
        ),
        migrations.RemoveField(
            model_name='item',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_spacial',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='is_spacial',
        ),
        migrations.RemoveField(
            model_name='quotationitem',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='quotationitem',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='quotationitem',
            name='is_spacial',
        ),
    ]
