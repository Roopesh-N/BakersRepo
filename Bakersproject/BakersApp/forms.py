from typing import Any
from django import forms
from BakersApp.models import UserModel

class loginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=UserModel
        fields=['Username','password']

class signupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    re_enter_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=UserModel
        exclude=('slug',)
    def clean(self):
        total_data=super().clean()
        uname=total_data['Username']
        pwd=total_data['password']
        rwd=total_data['re_enter_password']
        fname=total_data['firstname']
        phone=total_data['PhoneNumber']
        if len(fname)<3:
            raise forms.ValidationError("Minimum Length of the first name should be 3 characters")
        if uname==fname :
            raise forms.ValidationError("username couldn't be same as firstname")
        if pwd!=rwd:
            raise forms.ValidationError("Both passwords should match")
        if pwd==uname:
            raise forms.ValidationError("Please choose different password")
        if len(str(phone))<8:
            raise forms.ValidationError("Please enter correct phone number")



