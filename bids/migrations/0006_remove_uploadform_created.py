# Generated by Django 3.0.7 on 2020-07-05 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0005_remove_uploadform_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadform',
            name='created',
        ),
    ]
