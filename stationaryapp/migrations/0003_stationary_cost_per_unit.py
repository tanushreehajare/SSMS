# Generated by Django 4.2.4 on 2023-09-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationaryapp', '0002_remove_assignment_assignment_sem'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationary',
            name='cost_per_unit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
