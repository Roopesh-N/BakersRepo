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

    
class CategoryModel(models.Model):
    category=models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return CategoryModel.objects.all()
    
    def __str__(self):
        return self.category
    

class ItemsModel(models.Model):
    itemName=models.CharField(max_length=40)
    price=models.IntegerField()
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='static/images/')
    
    @staticmethod
    def get_all_products():
        return ItemsModel.objects.all()
    




