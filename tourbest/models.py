from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    sales_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Style(models.Model):
    title = models.CharField(max_length=40)

class Tour(models.Model):
    title = models.CharField(max_length=50)
    style = models.ForeignKey(Style)
    price = models.IntegerField()
    location = models.CharField(max_length=50)
    duration = models.IntegerField()
    hot = models.BooleanField()
    available_count = models.IntegerField()
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    contact_phone = models.CharField(max_length=20)

class Bookings(models.Model):
    user = models.ForeignKey(UserProfile)
    tour = models.ForeignKey(Tour)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
