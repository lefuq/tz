# Generated by Django 3.0.7 on 2020-07-05 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0004_bidding_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadform',
            name='title',
        ),
    ]