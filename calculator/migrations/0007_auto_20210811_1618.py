# Generated by Django 3.2.5 on 2021-08-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_alter_elementsconsuption_culture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elementsconsuption',
            old_name='MgO',
            new_name='Mg',
        ),
        migrations.AlterField(
            model_name='graph',
            name='graph_img',
            field=models.ImageField(blank=True, upload_to='graphs'),
        ),
    ]
