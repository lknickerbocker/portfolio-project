from django.db import models
import datetime


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200) 
    body = models.TextField(max_length=1000)
    pub_date = models.DateTimeField()
    