"""TODOSOFTWARE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views import static
from django.conf import settings

from Leader import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
     path('admin/', admin.site.urls),
     path('',views.login,name='login'),
    path('admin',views.admin,name='admin'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('work',views.work,name='work'),
    path('landing',views.landing,name='landing'),
    path('superregister',views.superregister,name='superregister'),
    path('superlogin',views.superlogin,name='superlogin'),
    path('showresults',views.showresults,name='showresults'),
    path('contact',views.contact,name='contact'),
    path('detail',views.detail,name='detail'),
    path('single',views.single,name='single'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
