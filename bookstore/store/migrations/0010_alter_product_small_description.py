# Generated by Django 4.2.5 on 2023-09-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_small_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='small_description',
            field=models.TextField(max_length=500),
        ),
    ]
