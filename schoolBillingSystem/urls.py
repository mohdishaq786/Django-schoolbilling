"""schoolBillingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from user import views as user_views
from django.urls import path

admin.site.site_header = "School billing system Admin"
admin.site.site_title = "School billing system Admin Portal"
admin.site.index_title = "Welcome to School billing system Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enrollment/', user_views.register, name='enrollment'),
    path('', user_views.home, name='home'),
    path('about', user_views.about, name='about'),
    path('login', user_views.login, name='login'),
    path('defaultor',user_views.defaultor,name='Defaultorlist'),
    path('contact',user_views.contact, name='contact')
 ]
