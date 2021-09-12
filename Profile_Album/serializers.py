from django.db import models
from rest_framework import serializers
from Profile_Album.models import Photo , Photo_Album_Data

class How_Many_Album(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['Album_Id','Album_Name','Album_Description']


class Photo_Album_Data_ser(serializers.ModelSerializer):
    # Image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Photo_Album_Data
        fields = ['_Album_Id','Image']


class All_Photo(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['Album_Id','Album_Name','Album_Description']
