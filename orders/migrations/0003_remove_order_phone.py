# Generated by Django 3.2.5 on 2021-08-24 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210824_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]
