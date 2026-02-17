from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from django.utils import timezone
from datetime import date
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def District(request):
    districtdata=tbl_district.objects.all()
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    if request.method=="POST":
        district=request.POST.get("txt_dist")
        districtcount=tbl_district.objects.filter(district_name=district).count()
        if districtcount>0:
            return render(request,"Admin/District.html",{'msg':"District already exist"})  
        else:
            tbl_district.objects.create(district_name=district)
            return render(request,"Admin/District.html",{'msg':"District Inserted"})
    else:
        return render(request,"Admin/District.html",{'districtdata':districtdata,'data':admindata})
def Category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("txt_cat")
        categorycount=tbl_category.objects.filter(category_name=category).count()
        if categorycount>0:
            return render(request,"Admin/Category.html",{'msg':"Category already exist"})
        else:
            tbl_category.objects.create(category_name=category)
            return render(request,"Admin/Category.html",{'msg':"Category Inserted"})
    else:
        return render(request,"Admin/Category.html",{'categorydata':categorydata})
def AdminReg(request):
    admindata=tbl_adminreg.objects.all()
    if request.method=="POST":
        admin_name=request.POST.get("txt_name")
        admin_email=request.POST.get("txt_email")
        admin_password=request.POST.get("txt_pass")
        admincount=tbl_adminreg.objects.filter(admin_email=admin_email).count()
        if admincount>0:
            return render(request,"Admin/AdminReg.html",{'msg':"Email already exist"})
        else:
            tbl_adminreg.objects.create(admin_name=admin_name,admin_email=admin_email,admin_password=admin_password)
            return render(request,"Admin/AdminReg.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/AdminReg.html",{'admindata':admindata})
def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")

def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("Admin:Category")

def deladmin(request,aid):
    tbl_adminreg.objects.get(id=aid).delete()
    return redirect("Admin:AdminReg")
def editdistrict(request,edid):
    editdata=tbl_district.objects.get(id=edid)
    if request.method=="POST":
        district=request.POST.get("txt_dist")
        editdata.district_name=district
        editdata.save()
        return redirect("Admin:District")
    else:
        return render(request,"Admin/District.html",{'editdata':editdata})
def editcategory(request,ecid):
    editdata=tbl_category.objects.get(id=ecid)
    if request.method=="POST":
        category=request.POST.get("txt_cat")
        editdata.category_name=category
        editdata.save()
        return redirect("Admin:Category")
    else:
        return render(request,"Admin/Category.html",{'editdata':editdata})
def editadmin(request,eid):
    editdata=tbl_adminreg.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pass")
        editdata.admin_name=name
        editdata.admin_email=email
        editdata.admin_password=password
        editdata.save()
        return redirect("Admin:AdminReg")
    else:
        return render(request,"Admin/AdminReg.html",{'editdata':editdata})

def Place(request):
    districtdata=tbl_district.objects.all()
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    place=tbl_place.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        place=request.POST.get("txt_place")
        placecount=tbl_place.objects.filter(place_name=place,district=district).count()
        if placecount>0:
            return render(request,"Admin/Place.html",{'msg':"Place already exist"})
        else:
            tbl_place.objects.create(place_name=place,district=district)
            return render(request,"Admin/Place.html",{'msg':"Place Inserted",})
    else:
        return render(request,"Admin/Place.html",{'districtdata':districtdata,'place':place,'data':admindata})
def editplace(request,epid):
    editdata=tbl_place.objects.get(id=epid)
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        editplace=request.POST.get("txt_place")
        editdata.place_name=editplace
        editdata.district=district
        editdata.save()
        return redirect("Admin:Place")
    else:
        return render(request,"Admin/Place.html",{'editdata':editdata,'districtdata':districtdata})
def delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:Place")
def subcategory(request):
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get("sel_category"))
        subcategory=request.POST.get("txt_subcat")
        subcategorycount=tbl_subcategory.objects.filter(subcategory_name=subcategory,category=category).count()
        if subcategorycount>0:
            return render(request,"Admin/SubCategory.html",{'msg':"Subcategory already exist"})
        else:
            tbl_subcategory.objects.create(subcategory_name=subcategory,category=category)
            return render(request,"Admin/SubCategory.html",{'msg':"Subcategory Inserted"})
    else:
        return render(request,"Admin/SubCategory.html",{'categorydata':categorydata,'subcategorydata':subcategorydata})
def editsubcategory(request,escid):
    editdata=tbl_subcategory.objects.get(id=escid)
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get("sel_category"))
        subcategory=request.POST.get("txt_subcat")
        editdata.subcategory_name=subcategory
        editdata.category=category
        editdata.save()
        return redirect("Admin:subcategory")
    else:
        return render(request,"Admin/SubCategory.html",{'editdata':editdata,'categorydata':categorydata})
def delsubcategory(request,dsid):
    tbl_subcategory.objects.get(id=dsid).delete()
    return redirect("Admin:subcategory")

def designation(request):
    desidata=tbl_designation.objects.all()
    if request.method=="POST":
        designation=request.POST.get("txt_designation")
        designationcount=tbl_designation.objects.filter(designation_name=designation).count()
        if designationcount>0:
            return render(request,"Admin/Designation.html",{'msg':"Designation already exist"})
        else:
            tbl_designation.objects.create(designation_name=designation)
            return render(request,"Admin/Designation.html",{'msg':"Designation inserted"})
    else:
        return render(request,"Admin/Designation.html",{'desidata':desidata})

def editdesignation(request,eid):
    editdesi=tbl_designation.objects.get(id=eid)

    if request.method=="POST":
        designation=request.POST.get("txt_designation")
        editdesi.designation_name=designation
        editdesi.save()
        return redirect("Admin:Designation")
    else:
        return render(request,"Admin/Designation.html",{'editdesi':editdesi})

def deldesignation(request,did):
    tbl_designation.objects.get(id=did).delete()
    return redirect("Admin:Designation")

def department(request):
    deptdata=tbl_department.objects.all()
    if request.method=="POST":
        department=request.POST.get("dept_name")
        departmentcount=tbl_department.objects.filter(department_name=department).count()
        if departmentcount>0:
            return render(request,"Admin/Department.html",{'msg':"Department already exist"})
        else:
            tbl_department.objects.create(department_name=department)
            return render(request,"Admin/Department.html",{'msg':"Department inserted"})
    else:
        return render(request,"Admin/Department.html",{'deptdata':deptdata})
    
def editdepartment(request,eid):
    editdept=tbl_department.objects.get(id=eid)
    if request.method=="POST":
        dept=request.POST.get("dept_name")
        editdept.department_name=dept
        editdept.save()
        return redirect("Admin:Department")
    else:
        return render(request,"Admin/Department.html",{'editdept':editdept})

def deldepartment(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect("Admin:Department")

def employee(request):
    deptdat=tbl_department.objects.all()
    desidata=tbl_designation.objects.all()
    empdata=tbl_employee.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("gender")
        contact=request.POST.get("txt_num")
        doj=request.POST.get("txt_doj")
        department=tbl_department.objects.get(id=request.POST.get("select_department"))
        designation=tbl_designation.objects.get(id=request.POST.get("select_designation"))
        salary=request.POST.get("txt_salary")
        employeecount=tbl_employee.objects.filter(employee_name=name).count()
        if employeecount>0:
            return render(request,"Admin/Employee.html",{'msg':"Employee already exist"})
        else:
            tbl_employee.objects.create(employee_name=name,employee_gender=gender,employee_contact=contact,employee_doj=doj,
            department=department,designation=designation,employee_salary=salary)
        return render(request,"Admin/Employee.html",{'msg':"Employee inserted"})
    else:
        return render(request,"Admin/Employee.html",{'deptdata':deptdat,'desidata':desidata,'empdata':empdata})


def editemployee(request,eid):
    deptdata=tbl_department.objects.all()
    desidata=tbl_designation.objects.all()
    editemp=tbl_employee.objects.get(id=eid)
    if request.method=="POST":
        department=tbl_department.objects.get(id=request.POST.get("select_department"))
        designation=tbl_designation.objects.get(id=request.POST.get("select_designation"))
        name=request.POST.get("txt_name")
        gender=request.POST.get("gender")
        contact=request.POST.get("txt_num")
        doj=request.POST.get("txt_doj")
        salary=request.POST.get("txt_salary")
        editemp.employee_name=name
        editemp.employee_gender=gender
        editemp.employee_contact=contact
        editemp.employee_doj=doj
        editemp.employee_salary=salary
        editemp.department=department
        editemp.designation=designation
        editemp.save()
        return redirect("Admin:Employee")
    else:
        return render(request,"Admin/Employee.html",{'deptdata':deptdata,'desidata':desidata,'editemp':editemp})


def delemployee(request,did):
    tbl_employee.objects.get(id=did).delete()
    return redirect("Admin:Employee")
def sellerlist(request):
    seller=tbl_seller.objects.all()
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    selleraccept=tbl_seller.objects.filter(seller_status=1)
    sellerreject=tbl_seller.objects.filter(seller_status=2)
    return render(request,"Admin/Sellerlist.html",{'seller':seller,'selleraccept':selleraccept,'sellerreject':sellerreject,'data':admindata})
def userlist(request):
    user=tbl_user.objects.all()
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    useraccept=tbl_user.objects.filter(user_status=1)
    userreject=tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/Userlist.html",{'userdata':user,'useraccept':useraccept,'userreject':userreject,'data':admindata})
def acceptseller(request,aid):
    data=tbl_seller.objects.get(id=aid)
    data.seller_status=1
    data.save()
    return render(request,"Admin/Sellerlist.html",{'msg':'verified'})
def rejectseller(request,rid):
    data=tbl_seller.objects.get(id=rid)
    data.seller_status=2
    data.save()
    return render(request,"Admin/Sellerlist.html",{'msg':'Rejected'})

def acceptuser(request,aid):
    data=tbl_user.objects.get(id=aid)
    data.user_status=1
    data.save()
    email=data.user_email
    send_mail(
    'Good News! Your Rent/Lease Request Is Approved 🎉',  # subject
    "Hello,\n\n"
    "We’re happy to let you know that your rent/lease request has been approved!\n\n"
    "✔ Your details have been verified successfully.\n"
    "✔ Your request meets our rental and lease guidelines.\n\n"
    "You can now move forward with the next steps and enjoy a smooth rental experience "
    "through Property Pulse.\n\n"
    "If you have any questions about rent, lease terms, or need help at any stage, "
    "our team is always here to assist you.\n\n"
    "Thank you for trusting Property Pulse to find the right place for you.\n\n"
    "Best wishes,\n"
    "Team Property Pulse",
    settings.EMAIL_HOST_USER,
    [email],
)

    return render(request,"Admin/Userlist.html",{'msg':"Accepted"})
    

def rejectuser(request,rid):
    data=tbl_user.objects.get(id=rid)
    data.user_status=2
    data.save()
    email=data.user_email
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rYour request was rejected because of"
        "\r1, You are not verified. "
        "\r2, if you have any queries, contact us."
        "\r By"
        "\r propertypulse" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,"Admin/Userlist.html",{'msg':'Rejected'})

def Homepage(request):
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    return render(request,"Admin/Homepage.html",{'data':admindata})

def Viewcomplaint(request):
    complaintdata=tbl_complaint.objects.filter(complaint_status=0)
    replied=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/Viewcomplaint.html",{'complaintdata':complaintdata,'replied':replied})

def Reply(request,cid):
    comdata=tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        reply=request.POST.get("txt_reply")
        comdata.complaint_reply=reply
        comdata.complaint_status=1
        comdata.save()
        return render(request,'Admin/Reply.html',{'msg':'Reply Sent'})
    else:
        return render(request,"Admin/Reply.html")
 
def ownerlist(request):
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    ownerdata=tbl_owner.objects.filter(owner_status=0)
    owneraccept=tbl_owner.objects.filter(owner_status=1)
    ownerreject=tbl_owner.objects.filter(owner_status=2)
    return render(request,"Admin/Ownerlist.html",{'ownerdata':ownerdata,'owneraccept':owneraccept,'ownerreject':ownerreject,'data':admindata})
def owneraccept(request,aid):
    data=tbl_owner.objects.get(id=aid)
    data.owner_status=1
    data.save()
    email=data.owner_email
    send_mail(
    'Owner Account Approved – Welcome to Property Pulse 🎉',  # subject
    "Hello,\n\n"
    "Great news! Your owner account has been successfully verified and approved.\n\n"
    "You now have full access to owner features on Property Pulse, including:\n"
    "• Adding and managing your property listings\n"
    "• Viewing and responding to booking requests\n"
    "• Managing rent and lease-related details\n\n"
    "You can log in and start using these features right away.\n\n"
    "If you need any assistance or have questions at any stage, feel free to reach out "
    "to our support team—we’re always happy to help.\n\n"
    "Thank you for being a part of Property Pulse.\n\n"
    "Best regards,\n"
    "Team Property Pulse" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,"Admin/Ownerlist.html",{'msg':'verified'})
def ownerreject(request,rid):
    data=tbl_owner.objects.get(id=rid)
    data.owner_status=2
    data.save()
    email=data.user_email
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rYour request was rejected because of"
        "\r1, You are not verified. "
        "\r2, if you have any queries, contact us."
        "\r By"
        "\r propertypulse" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,"Admin/Ownerlist.html",{'msg':'Rejected'})    

def propertytype(request):
    propertydata=tbl_propertytype.objects.all()
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    if request.method=="POST":
        propertytype=request.POST.get("txt_propertytype")
        propertytypecount=tbl_propertytype.objects.filter(propertytype_name=propertytype).count()
        if propertytypecount>0:
            return render(request,"Admin/Propertytype.html",{'msg':"Property Type already exist"})
        else:
            tbl_propertytype.objects.create(propertytype_name=propertytype)
        return render(request,"Admin/Propertytype.html",{'msg':"Property Inserted"})
    else:
        return render(request,"Admin/Propertytype.html",{'propertydata':propertydata,'data':admindata})

def editpropertytype(request,ptid):
    editdata=tbl_propertytype.objects.get(id=ptid)
    if request.method=="POST":
        propertytype=request.POST.get("txt_propertytype")
        editdata.propertytype_name=propertytype
        editdata.save()
        return redirect("Admin:propertytype")
    else:
        return render(request,"Admin/Propertytype.html",{'editdata':editdata})
def delpropertytype(request,ptid):
    tbl_propertytype.objects.get(id=ptid).delete()
    return redirect("Admin:propertytype")

def viewservices(request):
    servicedata=tbl_servicerequest.objects.all()
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    return render(request,"Admin/Viewservices.html",{'servicedata':servicedata,'data':admindata})

def acceptservice(request,sid):
    data=tbl_servicerequest.objects.get(id=sid)
    data.servicerequest_status=1
    data.save()
    return redirect("Admin:viewservices")

def rejectservice(request,sid):
    data=tbl_servicerequest.objects.get(id=sid)
    data.servicerequest_status=2
    data.save()
    return redirect("Admin:viewservices")

def serviceamount(request,sid):
    servicedata=tbl_servicerequest.objects.get(id=sid)
    if request.method=="POST":
        amount=request.POST.get("txt_amount")
        reply=request.POST.get("txt_reply")
        servicedata.servicerequest_reply=reply
        servicedata.servicerequest_amount=amount
        servicedata.save()
        return render(request,"Admin/Serviceamount.html",{'msg':'Amount Sent to User'})
    else:
        return render(request,"Admin/Serviceamount.html",{'data':servicedata})

def logout(request):
    del request.session['aid']
    return redirect("Guest:Login")


def AdminDashboard(request):
    pending_count = tbl_request.objects.filter(request_status=0).count()
    approved_count = tbl_request.objects.filter(request_status=1).count()
    sold_count = tbl_request.objects.filter(request_status=3).count()

    context = {
        "pie_labels": ["Pending", "Approved", "Sold"],
        "pie_data": [pending_count, approved_count, sold_count],
    }

    return render(request, "Admin/Homepage.html", context)
    