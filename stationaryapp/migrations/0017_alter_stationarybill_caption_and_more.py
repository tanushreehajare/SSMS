# Generated by Django 4.2.4 on 2024-02-17 17:22

from django.db import migrations, models
import stationaryapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('stationaryapp', '0016_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationarybill',
            name='caption',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='stationarybill',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=stationaryapp.models.filepath),
        ),
    ]
