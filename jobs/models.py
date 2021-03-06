from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    linktoarticle = models.CharField(max_length=1000)
    placeholder = models.IntegerField(default=1)
