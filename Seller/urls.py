from django.urls import path
from Seller import views
app_name="Seller"
urlpatterns = [
    path('Profile/',views.Profile,name="Profile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Homepage/',views.Homepage,name="Homepage"),
    
    
]