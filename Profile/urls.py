from django.urls import path ,include
from . import views


urlpatterns = [
    path('register', views.register),
    path('register_data', views.register_data),
    path('logout', views.logout_view),
]