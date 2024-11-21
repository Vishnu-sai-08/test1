"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('eve1',views.ev1),
    path('login/',views.log),
    path('register/',views.reg),
    path('',views.mia),
    path('contact/',views.cont),
    path('about-us/',views.abo),
    path('doregister/',views.doreg),
    path('logincheck/',views.logincheck),
    path('userhome/',views.use),
    path('adminhome/',views.adm),
    path('Viewusers/',views.vus),
    path('modify/',views.modi),


]
