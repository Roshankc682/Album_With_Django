from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Profile.urls')),
    path('', include('Profile_Album.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
