from django.db import models

# Create your models here.
class PersonalData(models.Model):
    name = models.CharField(max_length=80,unique=True)
    birth = models.DateField()
    greetings = models.CharField(max_length=100,default="Greetings")
    intro_text = models.TextField(default="Intro Text")
    location = models.CharField(max_length=30,default="Toronto, ON")
    loc_icon = models.CharField(max_length=100,default="images/location-icon")

class SocialMedia(models.Model):
    social = models.CharField(max_length=30,unique=True)
    link = models.CharField(max_length=70)
    image_path = models.CharField(max_length=256,default="images/notfound.jpg")
    target = models.CharField(max_length=15,default="_blank")
    order = models.IntegerField(default=100)

class PersonalDescription(models.Model):
    category = models.CharField(max_length=30,unique=True)
    description = models.TextField()
    active = models.CharField(max_length=10,blank=True)
    checked = models.CharField(max_length=10,blank=True)
    hide = models.CharField(max_length=20,blank=True)
    order = models.IntegerField(default=100)
