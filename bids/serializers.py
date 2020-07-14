from rest_framework import serializers
from .models import *
from django.core.files.base import File

class BiddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidding
        fields = '__all__'

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadForm
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadForm
        fields = '__all__'
