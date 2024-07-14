from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    List_display = ['user', 'phone_number', 'address']
    raw_id_fields = ['user',]
