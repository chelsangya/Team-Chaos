from django.db import models

# Create your models here.
class Safety(models.Model):
    sID = models.AutoField(primary_key=True)
    issueType = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    uID = models.IntegerField()