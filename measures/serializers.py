from rest_framework import serializers
from .models import Measures, UserAttributes
from .service import calculate_tmb

class UserAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAttributes
        fields = '__all__'


class MeasuresSerializer(serializers.ModelSerializer):
    tmb = serializers.SerializerMethodField()

    class Meta:
        model = Measures
        fields = '__all__'

    def get_tmb(self, obj):
        gender = obj.user.userattributes.gender
        birth_date = obj.user.userattributes.birth_date

        created_at = obj.created_at
        height = obj.height
        weight = obj.weight

        return calculate_tmb(gender, birth_date, created_at, height, weight)