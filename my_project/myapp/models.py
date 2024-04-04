from django.db import models

# Create your models here.
class subject(models.Model):
    subjectid = models.IntegerField()
    subjectname= models.CharField(max_length=20)
    subjectmark = models.CharField(max_length=20)
    subjectmedium = models.CharField(max_length=20)