# Generated by Django 2.2.7 on 2019-11-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='comodidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
