"""sinek_tasarim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from products.views import (index, products_view, register_user, login_user, logout_user, product_detail, product_like)

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^products/(?P<product_id>[0-9]+)/$', product_detail,name= 'product_detail'),
    url(r'^products$', products_view, name='products'),
    url(r'^login', login_user, name='login'),
    url(r'^register$', register_user, name='register'),
    url(r'^logout', logout_user, name='logout'),
    url(r'^products/(?P<product_id>[0-9]+)/like$', product_like, name='like'),
    url(r'^admin/', include(admin.site.urls)),

]


