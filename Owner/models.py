from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_property(models.Model):
    property_title=models.CharField(max_length=100)
    property_details=models.CharField(max_length=500)
    property_date=models.DateField(auto_now_add=True)
    property_status=models.IntegerField(default=0)
    property_photo=models.FileField(upload_to='Assets/PropertyPhotos/')
    propertytype_id=models.ForeignKey(tbl_propertytype,on_delete=models.CASCADE)
    owner=models.ForeignKey(tbl_owner,on_delete=models.CASCADE) 
    property_amount=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    gallery_photo=models.FileField(upload_to='Assets/GalleryPhotos/')
    property=models.ForeignKey(tbl_property,on_delete=models.CASCADE)
