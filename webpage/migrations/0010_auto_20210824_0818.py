# Generated by Django 3.2.5 on 2021-08-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0009_elementsdescription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementsdescription',
            options={'verbose_name': 'Описание элемента', 'verbose_name_plural': 'Описание элементов'},
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='B',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Ca',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Co',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Cu',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Fe',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='K',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Mg',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Mn',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Mo',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='N',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='P',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='S',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Se',
        ),
        migrations.RemoveField(
            model_name='elementsdescription',
            name='Zn',
        ),
        migrations.AddField(
            model_name='elementsdescription',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание элемента'),
        ),
        migrations.AddField(
            model_name='elementsdescription',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Название элемента'),
        ),
    ]
