from django.db import models
from Admin.models import *


# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_image=models.FileField(upload_to='Assets/UserDocs/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_status=models.IntegerField(default=0)

class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=50)
    seller_contact=models.CharField(max_length=50)
    seller_email=models.CharField(max_length=50)
    seller_password=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    estd_date=models.CharField(max_length=50)
    license_num=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=50)
    license_proof=models.FileField(upload_to='Assets/SellerDocs/')
    owner_proof=models.FileField(upload_to='Assets/SellerDocs/')
    seller_status=models.IntegerField(default=0)

class tbl_owner(models.Model):
    owner_name=models.CharField(max_length=50)
    owner_email=models.CharField(max_length=50)
    owner_contact=models.CharField(max_length=50)
    owner_address=models.CharField(max_length=50)
    owner_photo=models.FileField(upload_to='Assets/OwnerDocs/')
    owner_proof=models.FileField(upload_to='Assets/OwnerDocs/')
    owner_password=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    owner_status=models.IntegerField(default=0)
    owner_doj=models.DateField(auto_now_add=True)
    

