# Generated by Django 3.0.7 on 2020-07-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadform',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='uploadform',
            name='file',
            field=models.FileField(upload_to='bids/upl/'),
        ),
    ]