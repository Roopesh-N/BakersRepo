from django.shortcuts import render
from BakersApp.forms import loginForm,signupForm
from BakersApp.models import UserModel
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect,HttpResponse,redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


#two lines belongs to sending email
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def LoginView(request):
    form=loginForm
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['password']
        form=loginForm(request.POST)
        if form.is_valid():
            try:
                user=UserModel.objects.get(Username=username)
                enc_pwd=user.password
                validated=validate_password(password,enc_pwd)
                if validated==False:
                    messages.error(request,"Incorrect password entered.Try again!")
                else:
                    # slug=user.slug
                    return HttpResponseRedirect(reverse('homepage'))
            except ObjectDoesNotExist:
                messages.error(request,"user doesn't exit. Try Entering correct username")
        
    return render(request,'BakersApp/loginpage.html',{'form':form})


def signupView(request):
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            username=request.POST['Username']
            password=request.POST['password']
            epwd=passlib_encryption(password)
            phone=request.POST['PhoneNumber']
            email=request.POST['Email']
            user=UserModel.objects.create(firstname=firstname,lastname=lastname,Username=username,password=epwd,PhoneNumber=phone,Email=email)
            subject = "welcome to Bakers'App world"
            message = f'Hi {user.firstname}, thank you for registering in BakersApp.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            try:
                send_mail( subject, message, email_from, recipient_list )
            except:
                pass
            messages.success(request,"Account created successfully, Please login")
            return redirect('login')
    return render(request,'BakersApp/signup.html',{'form':form})

from passlib.hash import pbkdf2_sha256
def passlib_encryption(raw_password):
    if raw_password:
        encrypted=pbkdf2_sha256.hash(raw_password)
    else:
        return None
    return encrypted

def validate_password(raw_password,encrypted_password):
    if raw_password and encrypted_password:
        response=pbkdf2_sha256.verify(raw_password,encrypted_password)
    else:
        response=None
    return response

def homepage_view(request):
    return render(request,'BakersApp/homepage.html')
