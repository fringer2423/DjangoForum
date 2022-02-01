from django.contrib import admin
from .models import Checkbox


@admin.register(Checkbox)
class CheckboxAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_checked']
