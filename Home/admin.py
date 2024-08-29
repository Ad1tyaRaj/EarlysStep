from django.contrib import admin
from .models import Suggested_Steps,Other_sec

# Register your models here.

@admin.register(Suggested_Steps)
class SuggestedAdmin(admin.ModelAdmin):
    list_display = ['title','stock_img']


@admin.register(Other_sec)
class Other_sec_Admin(admin.ModelAdmin):
    list_display = ['card_title','card_discription','card_img']
