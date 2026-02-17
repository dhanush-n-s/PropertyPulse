from django.shortcuts import render,redirect
from User.models import  *
from Guest.models import  *
from Admin.models import  *
from Owner.models import  *
from django.db.models import Sum
from django.http import JsonResponse



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
        ar=[1,2,3,4,5]
        parry=[]
        propertydata=tbl_property.objects.all()

        for i in propertydata:
            tot=0
            ratecount=tbl_rating.objects.filter(propertyid=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(propertyid=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
        datas=zip(propertydata,parry)
        return render(request,"User/Viewproperty.html",{'propertydata':datas,'ar':ar})

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
        bookingdata=tbl_request.objects.filter(userid=request.session['uid'],request_status=3)
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

def viewservicerequestppt(request,rid):
        if "uid" not in request.session:
            return redirect("Guest:Login")
        else:
            servicerequestdata=tbl_servicerequest.objects.filter(requestid=rid)
            return render(request,"User/Myrequestppt.html",{'servicerequestdata':servicerequestdata})

def logout(request):
    del request.session['uid']
    return redirect("Guest:Login")

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(propertyid=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(propertyid=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    userid=tbl_user.objects.get(id=request.session['uid'])
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(userid=userid,user_name=user_name,user_review=user_review,rating_data=rating_data,propertyid=tbl_property.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(propertyid=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(propertyid=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(propertyid=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)