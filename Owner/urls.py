from django.urls import path # type: ignore
from Owner import views
app_name="Owner"

urlpatterns = [
    path('Homepage/',views.homepage,name="Homepage"),
    path('Profile/',views.Profile,name="Profile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('property/',views.property,name="property"),
    path('delproperty/<int:pid>/',views.delproperty,name="delproperty"),
    path('gallery/<int:oid>/',views.gallery,name="gallery"),
    path('delgallery/<int:did>/<int:oid>',views.delgallery,name="delgallery"),
    path('viewbookings/',views.viewbookings,name="viewbookings"),
    path('acceptbooking/<int:bid>/',views.acceptbooking,name="acceptbooking"),
    path('rejectbooking/<int:bid>/',views.rejectbooking,name="rejectbooking"),
    path('logout/',views.logout,name="logout"),
]