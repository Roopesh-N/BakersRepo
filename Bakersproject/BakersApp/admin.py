from django.contrib import admin
from BakersApp.models import UserModel,CategoryModel,ItemsModel

# Register your models here.
class userModelAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','Username','PhoneNumber','Email','password']
    prepopulated_fields={'slug':('firstname','lastname')}

admin.site.register(UserModel,userModelAdmin)

#admin class for categoryModel
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category']

admin.site.register(CategoryModel,CategoryAdmin)

#admin class for products
class productsAdmin(admin.ModelAdmin):
    list_display=['id','itemName','price','category','img']
    
admin.site.register(ItemsModel,productsAdmin)



