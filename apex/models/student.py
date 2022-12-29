from django.db import models
CATEGORY_CHOICES=[
    ('GEN','General'),
    ('SC','SC'),
    ('ST','ST'),
    ('OBC','OBC'),
    ('OTH',"OTHER"),
]
CERTIFICATE_STATUS_CHOICES=[
    ('RECIEVED','RECEIVED'),
    ('READY','READY'),
    ('IN_PROGRESS','IN PROGRESS'),
    ('NOT_INITIATED','NOT INITAIATED'),
]

class Student(models.Model):
    name=models.CharField(max_length=200)
    father_name=models.CharField(max_length=200)
    email=models.EmailField(blank=True,null=True)
    mobile_nnumber=models.CharField(max_length=15,blank=True,null=True)
    category=models.CharField(max_length=3,choices=CATEGORY_CHOICES)
    course=models.ForeignKey('Course',on_delete=models.CASCADE)
    registration_number=models.CharField(max_length=50,primary_key=True)
    certificate_status=models.CharField(max_length=15,choices=CERTIFICATE_STATUS_CHOICES)

