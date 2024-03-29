"""
URL configuration for two project.

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
from django.urls import path,include
from track.views import *
from django.contrib import admin,auth
urlpatterns = [
    path('admin/', admin.site.urls),
    path('track',include('track.urls')),
    path('pare', parent, ),
    path('product',productall,name='product' ),
    path('<int:id>',producrshow,name='proshow'),
    path('Add', productAdd, name='productAdd'),
path('Delete/<int:id>',productdel,name='prodel'),
path('update/<int:id>',productupdate,name='proupdate'),
    path('AddForm', productAddusingForm, name='productAddusingForm'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile',productall)

]
