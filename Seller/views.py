from django.shortcuts import render
from User.models import *
from Guest.models import *
from Admin.models import *

# Create your views here.
def Profile(request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,"Seller/Profile.html",{'data':sellerdata})


def EditProfile(request):
    profiledata=tbl_seller.objects.get(id=request.session['sid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        date=request.POST.get('txt_date')
        lisencenum=request.POST.get('txt_lno')
        licensproof=request.POST.get('txt_lp')
        idproof=request.POST.get('txt_ip')
        ownername=request.POST.get('txt_on')
        profiledata.seller_name=name
        profiledata.seller_email=email
        profiledata.seller_contact=contact
        profiledata.estd_date=date
        profiledata.license_num=lisencenum
        profiledata.owner_name=ownername
        profiledata.save()
        return render(request,"Seller/EditProfile.html",{'msg':'Updated'})
    else:
        return render(request,"Seller/EditProfile.html",{'Data':profiledata})

def ChangePassword(request):
    profiledata=tbl_seller.objects.get(id=request.session['sid'])
    dbpass=profiledata.seller_password
    if request.method=="POST":
        old=request.POST.get('txt_old')
        new=request.POST.get('txt_new')
        confirm=request.POST.get('txt_re')
        if old==dbpass:
            if new==confirm:
                profiledata.seller_password=new
                profiledata.save()
                return render(request,"Seller/Profile.html",{'msg':'Updated'})
            else:
                return render(request,"Seller/EditProfile.html",{'msg':'Updated'})
        else:
            return render(request,"Seller/EditProfile.html",{'Data':profiledata})
    return render(request,"Seller/Changepassword.html")

def Homepage(request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,"Seller/Homepage.html",{'data':sellerdata})