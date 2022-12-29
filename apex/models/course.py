from django.db import models

class Course(models.Model):
    name=models.CharField( max_length=200)
    duration=models.CharField( max_length=50)
    features=models.CharField( max_length=300,blank=True,null=True)
    price_for_gen=models.IntegerField(blank=True,null=True)
    price_for_sc=models.IntegerField(blank=True,null=True)
    price_for_st=models.IntegerField(blank=True,null=True)
    price_for_obc=models.IntegerField(blank=True,null=True)
