from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
 path('NewUser/',views.newuser,name="NewUser"),
 path('AjaxPlace/',views.AjaxPlace,name='AjaxPlace'),
 path('Login/',views.Login,name="Login"),
 path('newseller/',views.newseller,name="newseller"),
 path('OwnerRegistration/',views.newowner,name="OwnerRegistration"),
 path('indexpage/',views.indexpage,name="indexpage"),
 path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),




]