from django.db import models
import datetime


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200) 
    body = models.TextField(max_length=1000)
    pub_date = models.DateTimeField()
    
    def __str__(self): ###object title in database
        return self.title
    
    def summary(self): ####createsanewbodylimited to 100 
        return self.body[:100]
    
    def pub_date_pretty(self): #customizes our date/time
        return self.pub_date.strftime('%b %e %Y')