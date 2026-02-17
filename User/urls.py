from django.urls import path # type: ignore
from User import views

app_name="User"

urlpatterns = [
  path('Profile/',views.Profile,name="Profile"),
  path('EditProfile/',views.EditProfile,name="EditProfile"),
  path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
  path('Homepage/',views.Homepage,name="Homepage"),
  path('Complaints/',views.Complaints,name="Complaints"),
  path('delcomp/<int:cid>/',views.delcomp,name="delcomp"),
  path('viewproperty/',views.viewproperty,name="viewproperty"),
  path('viewgallery/<int:pid>/',views.viewgallery,name="viewgallery"),
  path('requestproperty/<int:pid>/',views.request,name="requestproperty"),
  path('mybookings/',views.mybookings,name="mybookings"),
  path('payment/<int:id>/',views.payment,name="payment"),
  path('Servicerequest/<int:rid>/',views.Servicerequest,name="Servicerequest"),
  path('servicepayment/<int:sid>/',views.servicepayment,name="servicepayment"),
  path('viewservicerequest/',views.viewservicerequest,name="viewservicerequest"), 
  path('viewservicerequestppt/<int:rid>/',views.viewservicerequestppt,name="viewservicerequestppt"), 
  path('logout/',views.logout,name="logout"),
  path('rating/<int:mid>',views.rating,name="rating"),  
  path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
  path('starrating/',views.starrating,name="starrating"),

]
    