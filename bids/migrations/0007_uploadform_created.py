# Generated by Django 3.0.7 on 2020-07-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0006_remove_uploadform_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadform',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
