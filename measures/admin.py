from django.contrib import admin
from .models import Measures

@admin.register(Measures)
class MeasuresAdmin(admin.ModelAdmin):
    list_display = ['user', 'height', 'weight', 'created_at', 'updated_at']
