from django.contrib import admin

from Profile_Album.models import  Photo , Photo_Album_Data

@admin.register(Photo)
class Photo(admin.ModelAdmin):
    list_display = ['Album_Id','Album_Name','Album_Description','user_id']


@admin.register(Photo_Album_Data)
class Photo_Album_Data(admin.ModelAdmin):
    list_display = ['id','_Album_Id','Image']




