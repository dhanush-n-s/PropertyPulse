from django.db import models
from User.models import *
from Guest.models import *
from Admin.models import *
from Owner.models import *

# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50,null=True)
    complaint_status=models.IntegerField(default=0)
    userid=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)
    request_advance=models.CharField(max_length=50)
    property=models.ForeignKey(tbl_property,on_delete=models.CASCADE)
    userid=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)
    propertyid=models.ForeignKey(tbl_property,on_delete=models.CASCADE)
    userid=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_servicerequest(models.Model):
    servicerequest_title=models.CharField(max_length=50)
    servicerequest_details=models.CharField(max_length=100)
    servicerequest_reply=models.CharField(max_length=100,null=True)
    requestid=models.ForeignKey(tbl_request,on_delete=models.CASCADE)
    servicerequest_date=models.DateField(auto_now_add=True)
    servicerequest_time=models.TimeField(auto_now_add=True)
    servicerequest_amount=models.CharField(max_length=50,null=True)
    servicerequest_status=models.IntegerField(default=0)

    
   