from rest_framework import serializers
from .models import Books
from django.conf import settings

class BooksSerializer(serializers.ModelSerializer):
    '''
    modelserializer for contentbrief
    '''

    class Meta:
        model = Books
        fields = '__all__'
