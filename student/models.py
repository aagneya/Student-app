from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50 , blank=True, null=True)
    address = models.CharField(max_length=300)
    interests = models.TextField()
    joining_date = models.DateTimeField(default=timezone.now)
    roll_no = models.IntegerField(default=0)
    course = models.CharField(max_length=300,default=0)
    image = models.FileField(upload_to ='uploadedimages',null = True)
    def __str__(self):
        return self.name

class mark(models.Model):
    title = models.CharField(max_length = 200 , null = True)
    image = models.FileField(upload_to ='uploadedimages',null = True)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
