from django.db import models


# Create your models here.



class Suggested_Steps(models.Model):
    title = models.CharField(max_length=100)
    stock_img =  models.FileField(upload_to='front-img/',max_length=250,null=True,default=None)


class Other_sec(models.Model):
    card_title = models.CharField(max_length=70)
    card_discription = models.CharField(max_length=110)
    card_img = models.FileField(upload_to='front-img/',max_length=250,null=True,default=None)

class Remides(models.Model):
    main_title = models.CharField(max_length=70)
    tamp_img = models.FileField(upload_to='Tamp/',max_length=250,null=True,default=None)
    tamp_discription = models.TextField(max_length=1000)
    short_discription = models.TextField(max_length=110)
    # sec-I
    step_img1 = models.FileField(upload_to='step_img/',max_length=250,null=True,default=None)
    step_title1 = models.CharField(max_length=70)
    step_discription1 = models.TextField(max_length=500)
    # sec-II
    step_img2 = models.FileField(upload_to='step_img/',max_length=250,null=True,default=None)
    step_title2 = models.CharField(max_length=70)
    step_discription2 = models.TextField(max_length=500)
    # sec-III
    step_img3 = models.FileField(upload_to='step_img/',max_length=250,null=True,default=None)
    step_title3 = models.CharField(max_length=70)
    step_discription3 = models.TextField(max_length=500)
    # sec-IV
    step_img4 = models.FileField(upload_to='step_img/',max_length=250,null=True,default=None)
    step_title4 = models.CharField(max_length=70)
    step_discription4 = models.TextField(max_length=500)
    # sec-V
    step_img5 = models.FileField(upload_to='step_img/',max_length=250,null=True,default=None)
    step_title5 = models.CharField(max_length=70)
    step_discription5 = models.TextField(max_length=500)
    # sec-VI
    step_img6 = models.FileField(upload_to='step_img/',max_length=250,null=True,default=None)
    step_title6 = models.CharField(max_length=70)
    step_discription6 = models.TextField(max_length=500)
    # sec-VII
    step_img7 = models.FileField(upload_to='step_img/',max_length=250,null=True,default=None)
    step_title7 = models.CharField(max_length=70)
    step_discription7 = models.TextField(max_length=500)
    # sec-VIII
    step_img8 = models.FileField(upload_to='step_img/',max_length=250,null=True,default=None)
    step_title8 = models.CharField(max_length=70)
    step_discription8 = models.TextField(max_length=500)