# Generated by Django 3.2.5 on 2021-07-27 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20210727_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaultelementsconcentration',
            old_name='NO',
            new_name='N',
        ),
        migrations.RenameField(
            model_name='elementsconsuption',
            old_name='NO',
            new_name='N',
        ),
    ]
