from django.conf.urls import url
from django.contrib import admin
from . import views

app_name='user'
urlpatterns = [
    url(r'^$', views.listitems, name='list'),
    url(r'^add/$', views.createpost, name='create'),
    url(r'^(?P<id>\d+)/edit/$', views.update, name='update'),
    url(r'^(?P<id>\d+)/$', views.postdetail, name='detail'),
    url(r'^(?P<id>\d+)/delete/$', views.delete, name='delete')
]
