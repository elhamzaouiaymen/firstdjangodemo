from django.conf.urls import url
from . import views

urlpatterns = [

    # defining an url pattern for : /music/
    url(r'^$', views.index, name="index" ),

    # defining an url pattern for : /music/album_id/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name="details"),
]