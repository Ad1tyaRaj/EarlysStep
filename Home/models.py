from django.db import models

# Create your models here.


class Suggested_Steps(models.Model):
    title = models.CharField(max_length=100)
    stock_img =  models.FileField(upload_to='profile_img/',max_length=250,null=True,default=None)