from django.contrib.auth import authenticate
from django.http import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404 , redirect
from rest_framework.generics import ListAPIView
from django.urls import reverse
from Profile_Album.models  import Photo , Photo_Album_Data
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.http import HttpResponse
from django.core import serializers
from Profile_Album.serializers import How_Many_Album , All_Photo , Photo_Album_Data_ser
from rest_framework import viewsets
from Profile.models  import Users
from rest_framework.response import Response

@login_required(redirect_field_name="next",login_url=None)
def Dashboard(request):
    if request.method == "POST":
        images = request.FILES.getlist('image_name')
        Album_Image_description = Photo.objects.create(Album_Name=request.POST["Album"],Album_Description=request.POST["Album_Description"],user_id=request.user.id)
        for image in images:
            Photo_Album_Data.objects.create(_Album_Id=Album_Image_description,Image=image)
        return render(request, "dashboard.html")
    else:
        return render(request, "dashboard.html")


@login_required(redirect_field_name="next",login_url=None)
def index(request):
    return render(request,'index.html')

@login_required(redirect_field_name="next",login_url=None)
def Details(request,uuid):
    print(uuid)
    return render(request,'details.html')

class Photo_Belongs_Read_Only(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        # print(self.request.user.id)
        queryset = super().get_queryset().filter(user_id=self.request.user.id)
        return queryset
    queryset = Photo.objects.all()
    serializer_class = How_Many_Album
    permission_classes=[IsAuthenticated]

class SingleViewSet(viewsets.ViewSet):
    def get_permissions(self):
            if self.action == 'retrieve':
                permission_classes = [IsAuthenticated]
            else:
                permission_classes = [IsAuthenticated]
            return [permission() for permission in permission_classes]
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            Album_Data = Photo.objects.get(Album_Id=pk)
            serializer = All_Photo(Album_Data)
            return Response(serializer.data)

    def list(self,request):
        album_id = request.GET["get"]
        Album = Photo_Album_Data.objects.all().filter(_Album_Id=album_id)
        serializer = Photo_Album_Data_ser(Album,many=True)
        return Response(serializer.data)