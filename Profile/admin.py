from django.contrib import admin
from Profile.models import  Users


@admin.register(Users)
class Users(admin.ModelAdmin):
    list_display = ['id','email','name','password','username','session_token','active','is_staff','is_superuser','created_at','updated_at']




