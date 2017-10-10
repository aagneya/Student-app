from django import forms

from .models import Student, UserProfile 
from .models import mark
from django.contrib.auth.models import User



class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'address','interests','joining_date','roll_no','roll_no','image',)

class markForm(forms.ModelForm):

    class Meta:
        model = mark
        fields = ('title', 'image',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
