# Generated by Django 3.0.7 on 2021-06-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noizedb', '0002_auto_20210604_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='Date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата проведения измерения'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='Time',
            field=models.TimeField(auto_now_add=True, verbose_name='Время проведения измерения'),
        ),
    ]
