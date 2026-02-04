from django.shortcuts import render,redirect
from User.models import  *
from Guest.models import  *
from Admin.models import  *
from Owner.models import  *

# Create your views here.
def homepage(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    else:
        ownerdata=tbl_owner.objects.get(id=request.session['oid'])
        return render(request,"Owner/Homepage.html",{'data':ownerdata})

def Profile(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    else:
        ownerdata=tbl_owner.objects.get(id=request.session['oid'])
        return render(request,"Owner/Profile.html",{'data':ownerdata})

def EditProfile(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    else:
        ownerdata=tbl_owner.objects.get(id=request.session['oid'])
        if request.method=="POST":
            name=request.POST.get('txt_name')
            contact=request.POST.get('txt_contact')
            email=request.POST.get('txt_email')
            address=request.POST.get('txt_address')
            ownerdata.owner_name=name
            ownerdata.owner_email=email
            ownerdata.owner_contact=contact
            ownerdata.owner_address=address
            ownerdata.save()
            return render(request,"Owner/Editprofile.html",{'msg':'Updated'})
        else:
            return render(request,"Owner/EditProfile.html",{'Data':ownerdata})
    
def ChangePassword(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    else:
        ownerdata=tbl_owner.objects.get(id=request.session['oid'])
        dbpass=ownerdata.owner_password
        if request.method=="POST":
            old=request.POST.get('txt_old')
            new=request.POST.get('txt_new')
            confirm=request.POST.get('txt_re')
            if old==dbpass:
                if new==confirm:
                    ownerdata.owner_password=new
                    ownerdata.save()
                    return render(request,"Owner/Profile.html",{'msg':'Updated'})
                else:
                    return render(request,"Owner/EditProfile.html",{'msg':'New passwords do not match'})
            else:
                return render(request,"Owner/EditProfile.html",{'Data':ownerdata,'msg':'Old password is incorrect'})
    return render(request,"Owner/Changepassword.html")

def property(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    else:
        propertydata=tbl_property.objects.filter(owner=request.session['oid'])
        propertytypedata=tbl_propertytype.objects.all()
        districtdata=tbl_district.objects.all()
        placedata=tbl_place.objects.all()
    
        if request.method=="POST":
            title=request.POST.get("txt_title")
            details=request.POST.get("txt_details")
            amount=request.POST.get("txt_price")
            ptype=tbl_propertytype.objects.get(id=request.POST.get("sel_propertytype"))
            place=tbl_place.objects.get(id=request.POST.get("sel_place"))
            photo=request.FILES.get("txt_photo")
            owner=tbl_owner.objects.get(id=request.session['oid'])
            tbl_property.objects.create(property_title=title,property_details=details,propertytype_id=ptype,property_photo=photo,owner=tbl_owner.objects.get(id=request.session['oid']),property_amount=amount,place=place)
            return render(request,"Owner/Property.html",{'msg':'Property Added'})
        else:
            return render(request,"Owner/Property.html",{'propertydata':propertydata,'propertytypedata':propertytypedata,'districtdata':districtdata,'placedata':placedata})
    
def delproperty(request,pid):
    tbl_property.objects.get(id=pid).delete()
    return redirect("Owner:property")

def gallery(request,oid):
    propertydata=tbl_property.objects.filter(owner=request.session['oid'])
    propertydata=tbl_property.objects.get(id=oid)
    gallerydata=tbl_gallery.objects.filter(property=propertydata)
    if request.method=="POST":
        photo=request.FILES.get("txt_photo")
        tbl_gallery.objects.create(gallery_photo=photo,property=propertydata)
        return render(request,"Owner/Gallery.html",{'msg':'Photo Added','oid':oid})
    else:
        return render(request,"Owner/Gallery.html",{'propertydata':propertydata,'gallerydata':gallerydata,'oid':oid})
    
def delgallery(request,did,oid):
    tbl_gallery.objects.get(id=did).delete()
    return redirect("Owner:gallery",oid)

def viewbookings(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        bookingdata=tbl_request.objects.filter(property__owner=request.session['oid'])
        return render(request,"Owner/Viewbooking.html",{'bookingdata':bookingdata})

def acceptbooking(request,bid):
    booking=tbl_request.objects.get(id=bid)
    booking.request_status=1
    booking.save()
    return redirect("Owner:viewbookings")

def rejectbooking(request,bid):
    booking=tbl_request.objects.get(id=bid)
    booking.request_status=2
    booking.save()
    return redirect("Owner:viewbookings") 

def logout(request):
    del request.session['oid']
    return redirect("Guest:Login") 