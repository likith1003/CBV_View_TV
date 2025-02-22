"""
URL configuration for project15 project.

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fbv_string, name='fbv_string'),
    path('cbv_string', cbv_string.as_view(), name='cbv_string'), 
    path('insert_school_fbv', insert_school_fbv, name='insert_school_fbv'),
    path('insert_school_cbv', insert_school_cbv.as_view(), name='insert_school_cbv'),
    path('template_view', template_view.as_view(),name='template_view'),
]
