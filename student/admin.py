from django.contrib import admin

# Register your models here.
from .models import Student
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Student)
