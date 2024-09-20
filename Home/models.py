from django.db import models

# Create your models here.


class Suggested_Steps(models.Model):
    title = models.CharField(max_length=100)
    stock_img =  models.FileField(upload_to='front-img/',max_length=250,null=True,default=None)


class Other_sec(models.Model):
    card_title = models.CharField(max_length=70)
    card_discription = models.CharField(max_length=110)
    card_img = models.FileField(upload_to='front-img/',max_length=250,null=True,default=None)

class Remides_tamp(models.Model):
    main_title = models.CharField(max_length=70)
    tamp_img = models.FileField(upload_to='Tamp/',max_length=250,null=True,default=None)
    tamp_discription = models.CharField(max_length=500)
