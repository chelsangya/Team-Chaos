from django.db import models

# Create your models here.

class User(models.Model):
    uID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    photo = models.ImageField(upload_to='media/', default='/static/images/icon.png')
    password = models.CharField(max_length=20)
    OTP = models.IntegerField(null=True)

class Safety(models.Model):
    sID = models.AutoField(primary_key=True)
    issueType = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    uID = models.IntegerField()