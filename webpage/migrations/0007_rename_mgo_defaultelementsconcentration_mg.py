# Generated by Django 3.2.5 on 2021-08-11 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_defaultelementsconcentration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaultelementsconcentration',
            old_name='MgO',
            new_name='Mg',
        ),
    ]