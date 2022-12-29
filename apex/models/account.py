from django.db import models

class Account(models.Model):
    student=models.ForeignKey('Student',on_delete=models.CASCADE,blank=True,null=True)
    payment=models.IntegerField()
    proof=models.FileField(upload_to='fee_proofs/%Y/%m',blank=True,null=True)
    is_new=models.BooleanField()
    course=models.ForeignKey('Course',on_delete=models.CASCADE,blank=True,null=True)