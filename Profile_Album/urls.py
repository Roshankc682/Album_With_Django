from django.urls import path ,include
from . import views
# from Profile_Album.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path

#creating routers
router = DefaultRouter()

router.register('_API_', views.Photo_Belongs_Read_Only,basename='CountAlbumReadOnly')
router.register('_single_', views.SingleViewSet,basename='Single Album')

urlpatterns = [
    path('', views.index),
    path('',include(router.urls)),
    path('accounts/profile/', views.Dashboard,name="Add_Album"),
    # path('Album/{uuid}/', views.Details),
    path('Album/<uuid:uuid>/',views.Details,name='post_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()