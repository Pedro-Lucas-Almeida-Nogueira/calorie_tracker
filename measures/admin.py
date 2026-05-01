from django.contrib import admin
from .models import Measures, UserAttributes

@admin.register(UserAttributes)
class UserAttributesAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'birth_date']


@admin.register(Measures)
class MeasuresAdmin(admin.ModelAdmin):
    list_display = ['user', 'height', 'weight', 'created_at', 'updated_at']
