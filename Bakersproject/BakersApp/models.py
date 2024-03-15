from django.db import models
from django.utils.text import slugify

# Create your models here.
class UserModel(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    Username=models.CharField(max_length=30)
    PhoneNumber=models.IntegerField()
    Email=models.CharField(max_length=40)
    password=models.CharField(max_length=50)
    slug=models.SlugField(default="",null=False)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.firstname[:2]+self.lastname[:2])
        super(UserModel,self).save(*args,**kwargs)
    





