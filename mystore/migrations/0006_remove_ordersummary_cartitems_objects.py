# Generated by Django 5.0.6 on 2024-10-02 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0005_alter_reviews_product_object'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordersummary',
            name='cartitems_objects',
        ),
    ]
