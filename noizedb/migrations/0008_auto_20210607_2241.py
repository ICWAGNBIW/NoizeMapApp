# Generated by Django 3.0.7 on 2021-06-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noizedb', '0007_auto_20210607_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='Chark',
            field=models.CharField(default='Отсутствует', max_length=100, verbose_name='Характер источника шума'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='From',
            field=models.CharField(default='Отсутствует', max_length=100, verbose_name='Происхождение шума'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='MNlevel',
            field=models.FloatField(null=True, verbose_name='Максимальный уровень шума'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='Nlevel',
            field=models.FloatField(verbose_name='Эквивалентный уровень шума'),
        ),
    ]
