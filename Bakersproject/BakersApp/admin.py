from django.contrib import admin
from BakersApp.models import UserModel

# Register your models here.
class userModelAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','Username','PhoneNumber','Email','password']
    prepopulated_fields={'slug':('firstname','lastname')}

admin.site.register(UserModel,userModelAdmin)
