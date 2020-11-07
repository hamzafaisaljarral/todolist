from django.conf.urls import url
from . import views
from todolist.views import index
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    #url(r'^todolist$', views.index),
    #url(r'^login$', views.login)
]