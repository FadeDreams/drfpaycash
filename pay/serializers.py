from rest_framework import serializers
from .models import Pay


class PaysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields = ['id', 'date', 'description', 'amount', 'category']
