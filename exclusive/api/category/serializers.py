from rest_framework import serializers
from .models import Category


#serialzer convert model to json format

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')