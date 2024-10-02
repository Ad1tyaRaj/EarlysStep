from django.contrib import admin
from .models import Suggested_Steps,Other_sec,Remides


# Register your models here.

@admin.register(Suggested_Steps)
class SuggestedAdmin(admin.ModelAdmin):
    list_display = ['id','title','stock_img']


@admin.register(Other_sec)
class Other_sec_Admin(admin.ModelAdmin):
    list_display = ['id','card_title','card_discription','card_img']

@admin.register(Remides)
class Remidis_tamp_Admin(admin.ModelAdmin):
    list_display = ['id','main_title','tamp_img','tamp_discription','short_discription','step_img1','step_title1','step_discription1'
                    ,'step_img2','step_title2','step_discription2','step_img3','step_title3','step_discription3'
                    ,'step_img4','step_title4','step_discription4','step_img5','step_title5','step_discription5'
                    ,'step_img6','step_title6','step_discription6','step_img7','step_title7','step_discription7'
                    ,'step_img8','step_title8','step_discription8']
