from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *


# Create your views here.
def newuser(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("gender")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_mail")
        password=request.POST.get("txt_pass")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        address=request.POST.get("txt_add")
        photo=request.FILES.get("txt_photo")
        newusercount=tbl_user.objects.filter(user_email=email).count()
        if newusercount>0:
            return render(request,"Guest/NewUser.html",{'msg':"User email already exist"})
        else:
            tbl_user.objects.create(user_name=name,user_gender=gender,user_contact=contact,user_email=email,user_password=password,place=place,user_address=address,user_image=photo)
        return render(request,"Guest/NewUser.html",{'msg':"User Inserted"})
    else:
        return render(request,"Guest/NewUser.html",{'districtdata':districtdata})
def AjaxPlace(request):
    districtid=request.GET.get('did')
    placedata=tbl_place.objects.filter(district=districtid)
    return render(request,'Guest/AjaxPlace.html',{'placedata':placedata})  

def Login(request):
    if request.method=="POST":
        email=request.POST.get("username")
        password=request.POST.get("pass")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_adminreg.objects.filter(admin_email=email,admin_password=password).count()
        sellercount=tbl_seller.objects.filter(seller_email=email,seller_password=password).count()
        ownercount=tbl_owner.objects.filter(owner_email=email,owner_password=password).count()
        if usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect("User:Homepage")
        elif admincount>0:
             admindata=tbl_adminreg.objects.get(admin_email=email,admin_password=password)
             request.session['aid']=admindata.id
             return redirect("Admin:Homepage")
        elif sellercount>0:
             sellerdata=tbl_seller.objects.get(seller_email=email,seller_password=password)
             request.session['sid']=sellerdata.id
             return redirect("Seller:Homepage")
        elif ownercount>0:
             ownerdata=tbl_owner.objects.get(owner_email=email,owner_password=password)
             request.session['oid']=ownerdata.id
             return redirect("Owner:Homepage")
        else:
            return render(request,"Guest/Login.html",{'msg':'invalid Login'})
    else:
        return render(request,"Guest/Login.html")

def newseller(request):
     districtdata=tbl_district.objects.all()
     placedata=tbl_place.objects.all()
     if request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_mail")
        password=request.POST.get("txt_pass")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        estd_date=request.POST.get("est_date")
        license_no=request.POST.get("txt_lic")
        owner_name=request.POST.get("own_name")
        license_proof=request.FILES.get("lic_proof")
        owner_proof=request.FILES.get("own_proof")
        newsellercount=tbl_seller.objects.filter(seller_email=email).count()
        if newsellercount>0:
            return render(request,"Guest/Newseller.html",{'msg':"Seller email already exist"})
        else:
            tbl_seller.objects.create(seller_name=name,seller_contact=contact,seller_email=email,seller_password=password,place=place,estd_date=estd_date,license_num=license_no,owner_name=owner_name,license_proof=license_proof,owner_proof=owner_proof)
        return render(request,"Guest/Newseller.html",{'msg':"Seller Inserted"})
     else:
        return render(request,"Guest/Newseller.html",{'placedata':placedata,'districtdata':districtdata})
def newowner(request):
        districtdata=tbl_district.objects.all()
        placedata=tbl_place.objects.all()
        if request.method=="POST":
            name=request.POST.get("txt_ownername")
            email=request.POST.get("txt_owneremail")
            contact=request.POST.get("txt_ownercontact")
            address=request.POST.get("txt_owneraddress")
            photo=request.FILES.get("txt_ownerphoto")
            proof=request.FILES.get("txt_ownerproof")
            password=request.POST.get("txt_ownerproof")
            place=tbl_place.objects.get(id=request.POST.get("sel_place"))
            owner_proof=request.FILES.get("txt_ownerproof")
            newownercount=tbl_owner.objects.filter(owner_email=email).count()
            if newownercount>0:
                return render(request,"Guest/OwnerRegistration.html",{'msg':"owner email already exist"})
            else:
                tbl_owner.objects.create(owner_name=name,owner_contact=contact,owner_email=email,owner_password=password,place=place,owner_proof=owner_proof,owner_photo=photo,owner_address=address)
            return render(request,"Guest/OwnerRegistration.html",{'msg':"owner Inserted"})
        else:
            return render(request,"Guest/OwnerRegistration.html",{'placedata':placedata,'districtdata':districtdata})


def indexpage(request):
    return render(request,"Guest/Index.html")