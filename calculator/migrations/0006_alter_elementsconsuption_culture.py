# Generated by Django 3.2.5 on 2021-08-11 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_defaultelementsconcentration'),
        ('calculator', '0005_delete_defaultelementsconcentration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementsconsuption',
            name='culture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webpage.culture'),
        ),
    ]