"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from first_app import views as v1
from second_app import views as v2
from third_app import views as v3
from basic_app import views as v4

urlpatterns = [
    path('', v4.index, name='index'),
    path('basic_app/', include('basic_app.urls')),
    path('four/', include('third_app.urls')),
    path('polo/', include('first_app.urls')),
    path('second/', v2.index, name='index_2'),
    path('shutter/', v3.baka, name='baka'),
    path('admin/', admin.site.urls, name='index_5'),
    path('formpage/', v2.form_name_view, name='form_name'),
    path('logout/', v4.user_logout, name='logout'),
    path('special/', v4.special, name='special')
]
