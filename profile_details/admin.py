from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mobile_number','dob','location']
    list_filter=['name']
    search_fields=['id']





admin.site.register(UserProfile,UserProfileAdmin)