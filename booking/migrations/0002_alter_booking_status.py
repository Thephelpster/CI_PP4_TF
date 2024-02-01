# Generated by Django 3.2.15 on 2024-02-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Awaiting confirmation', 'Awaiting Confirmation'), ('Booking Confirmed', 'Booking Confirmed'), ('Booking Rejected', 'Booking Rejected'), ('Booking Expired', 'Booking Expired')], default='Awaiting confirmation', max_length=25),
        ),
    ]
