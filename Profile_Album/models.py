from django.conf.urls import url
from django.db import models
from django.urls import reverse
import uuid
import random , os
from Profile.models  import Users

def photo_path(instance, filename):
    file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(10))
    randomstr_name = randomstr
    return 'images/{randomstring}{ext}'.format(randomstring= randomstr_name, ext= file_extension)

class Photo(models.Model):
    Album_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Album_Name = models.CharField(max_length=100, blank=False,null=False)
    user_id = models.CharField(max_length=100, blank=False,null=False)
    Album_Description = models.TextField(max_length=1000, blank=False,null=False)

    # def get_absolute_url(self):
    #     return reverse("books:books-single", kwargs={"id": self.id})

class Photo_Album_Data(models.Model):
    _Album_Id = models.ForeignKey(Photo,related_name='All_data', on_delete=models.CASCADE,unique=False)
    Image= models.ImageField(upload_to=photo_path, null=False)

    def save(self, *args, **kwargs):
        super(Photo_Album_Data,self).save(*args,**kwargs)

