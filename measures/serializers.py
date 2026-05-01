from rest_framework import serializers
from .models import Measures, UserAttributes

class UserAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAttributes
        fields = '__all__'


class MeasuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measures
        fields = '__all__'