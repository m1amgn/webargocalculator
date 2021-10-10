# Generated by Django 3.2.5 on 2021-08-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0010_auto_20210825_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementsconsuption',
            name='B',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Ca',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Co',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Cu',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Fe',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='K',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Mg',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Mn',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Mo',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='N',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Ni',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='P',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='S',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Se',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='elementsconsuption',
            name='Zn',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
    ]
