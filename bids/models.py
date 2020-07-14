from django.db import models
from datetime import datetime

class Bidding(models.Model):
    title = models.CharField(max_length = 50, default = '')
    customer = models.CharField(max_length = 50)
    item = models.CharField(max_length = 50)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()
    new = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class UploadForm(models.Model):
    file = models.FileField(upload_to = 'bids/upl/')
    created = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        super(UploadForm, self).save(*args, **kwargs)
