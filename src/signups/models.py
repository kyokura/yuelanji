from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
class SignUp(models.Model):
    
    email=models.EmailField()
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.email)
    
class Marticle(models.Model):
    title= models.CharField (max_length=100) #title
    category= models.CharField (max_length=50, blank=True) #tag
    tagshow=models.CharField(max_length=50, blank=True)
    date_time=models.DateTimeField (auto_now_add=True)
    content =models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
class Sarticle(models.Model):
    title= models.CharField (max_length=100) #title
    category= models.CharField (max_length=50, blank=True) #tag
    tagshow=models.CharField(max_length=50, blank=True)
    date_time=models.DateTimeField (auto_now_add=True)
    content =models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title    