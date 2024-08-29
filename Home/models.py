from django.db import models

# Create your models here.


class Suggested_Steps(models.Model):
    title = models.CharField(max_length=100)
    stock_img =  models.FileField(upload_to='profile_img/',max_length=250,null=True,default=None)


class Other_sec(models.Model):
    card_title = models.CharField(max_length=70)
    card_discription = models.CharField(max_length=110)
    card_img = models.FileField(upload_to='profile_img/',max_length=250,null=True,default=None)
