# Generated by Django 3.0.7 on 2021-06-06 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noizedb', '0005_auto_20210605_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noizedb.Coordinates'),
        ),
    ]
