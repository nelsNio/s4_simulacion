# Generated by Django 2.2.7 on 2019-11-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_auto_20191121_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tiempo_total_cliente',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='tiempo_total_limpieza',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='tiempo_total_servicio',
            field=models.TimeField(),
        ),
    ]
