from django.contrib import admin

# Register your models here.

from .models import  UserProfile, Tour, Style

admin.site.register(UserProfile)
admin.site.register(Tour)
admin.site.register(Style)
