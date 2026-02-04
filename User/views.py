from django.shortcuts import render,redirect
from User.models import  *
from Guest.models import  *
from Admin.models import  *
from Owner.models import  *




# Create your views here.
def Profile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,"User/Profile.html",{'Data':userdata})
    
def EditProfile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contact=request.POST.get("txt_contact")
            address=request.POST.get("txt_address")
            userdata.user_name=name
            userdata.user_email=email
            userdata.user_contact=contact
            userdata.user_address=address
            userdata.save()
            return render(request,"User/EditProfile.html",{'msg':'Data updated'})
        else:
            return render(request,"User/EditProfile.html",{'Data':userdata})

def ChangePassword(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")

    userdata = tbl_user.objects.get(id=request.session['uid'])

    if request.method == "POST":
        old_password = request.POST.get("txt_old")
        new_password = request.POST.get("txt_new")
        confirm_password = request.POST.get("txt_re")

        if userdata.user_password == old_password:
            if new_password == confirm_password:
                userdata.user_password = new_password
                userdata.save()
                return render(
                    request,
                    "User/ChangePassword.html",
                    {"msg": "Password updated successfully!"}
                )
            else:
                return render(
                    request,
                    "User/ChangePassword.html",
                    {"msg": "New passwords do not match!"}
                )
        else:
            return render(
                request,
                "User/ChangePassword.html",
                {"msg": "Old password is incorrect!"}
            )

    return render(request, "User/ChangePassword.html")


def Homepage(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,"User/Homepage.html",{'Data':userdata})

def Complaints(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata = tbl_user.objects.get(id=request.session['uid'])
        complaintdata=tbl_complaint.objects.filter(userid=request.session['uid'])
        if request.method=="POST":
            title=request.POST.get("txt_title")
            content=request.POST.get("txt_content")
            tbl_complaint.objects.create(complaint_title=title,complaint_content=content,userid=userdata)
            return render(request,"User/Complaint.html",{'msg':'complaint registered!'})
        else:
            return render(request,"User/Complaint.html",{'data':userdata,'complaintdata':complaintdata})
def delcomp(request,cid):
    tbl_complaint.objects.get(id=cid).delete()
    return redirect("User:Complaints")

def viewproperty(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        propertydata=tbl_property.objects.all()
        return render(request,"User/Viewproperty.html",{'propertydata':propertydata})

def viewgallery(request,pid):
    gallerydata=tbl_gallery.objects.filter(property=pid)
    return render(request,"User/Viewgallery.html",{'gallerydata':gallerydata})

def request(request,pid):
    property=tbl_property.objects.get(id=pid)
    tbl_request.objects.create(property=property,userid=tbl_user.objects.get(id=request.session['uid']))
    return redirect("User:viewproperty")

def mybookings(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        bookingdata=tbl_request.objects.filter(userid=request.session['uid'],request_status=1)
        bookingpending=tbl_request.objects.filter(userid=request.session['uid'],request_status=0)
        return render(request,"User/Mybooking.html",{'bookingdata':bookingdata,'bookingpending':bookingpending})
    
def payment(request,id):
    requestdata=tbl_request.objects.get(id=id)
    if request.method=="POST":
        amount=request.POST.get("txt_amount")
        requestdata.request_advance=amount
        requestdata.request_status=3
        requestdata.save()
        return render(request,"User/Payment.html",{'msg':'Payment Successful!'})
    else:
        return render(request,"User/Payment.html",{'data':requestdata})
def Servicerequest(request,rid):
    requestdata=tbl_request.objects.get(id=rid)
    if request.method=="POST":
        title=request.POST.get("txt_title")
        details=request.POST.get("txt_details")
        tbl_servicerequest.objects.create(servicerequest_title=title,servicerequest_details=details,requestid=requestdata)
        return render(request,"User/Servicerequest.html",{'msg':'Service Request Sent'})
    else:
        return render(request,"User/Servicerequest.html",{})
    
def servicepayment(request,sid):
    servicerequestdata=tbl_servicerequest.objects.get(id=sid)
    if request.method=="POST":
        amount=request.POST.get("txt_amount")
        servicerequestdata.servicerequest_amount=amount
        servicerequestdata.servicerequest_status=3
        servicerequestdata.save()
        return render(request,"User/Servicepayment.html",{'msg':'Payment Successful'})
    else:
        return render(request,"User/Servicepayment.html",{'data':servicerequestdata})
    
def viewservicerequest(request):
        if "uid" not in request.session:
            return redirect("Guest:Login")
        else:
            servicerequestdata=tbl_servicerequest.objects.filter(requestid__userid=request.session['uid'])
            return render(request,"User/Myrequest.html",{'servicerequestdata':servicerequestdata})

def logout(request):
    del request.session['uid']
    return redirect("Guest:Login")