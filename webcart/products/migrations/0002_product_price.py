# Generated by Django 2.1.4 on 2019-03-24 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=200.0, max_digits=10),
        ),
    ]
