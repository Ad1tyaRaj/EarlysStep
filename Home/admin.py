from django.contrib import admin
from .models import Suggested_Steps

# Register your models here.

@admin.register(Suggested_Steps)
class SuggestedAdmin(admin.ModelAdmin):
    list_display = ['title','stock_img']
