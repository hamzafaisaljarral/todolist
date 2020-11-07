"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from todolist.views import index
from register import urls
from register.views import register
from register.views import login
from todolist.views import edit_item

urlpatterns = [
    url(r'^$', include('register.urls')),
    url(r'^register$', register),
    url(r'^login$', login),
    url(r'^admin/', admin.site.urls),
    url(r'^todolist/', index, name="TodoList"),
    url(r'^edititem/(?P<id>\d+)$',edit_item,name='edititem')
    
]
