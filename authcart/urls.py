from django.urls import path
from authcart import views

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="handlelogin"),
    path("logout",views.logout,name="handlelogout"),
   
]
