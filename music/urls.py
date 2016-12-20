from django.conf.urls import url
from . import views
app_name='music'
urlpatterns = [


    # defining an url pattern for : /music/
    url(r'^$', views.index, name="index" ),

    # defining an url pattern for : /music/album_id/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name="detail"),

    # defining an url pattern for : /music/album_id/favourite
    url(r'^(?P<album_id>[0-9]+)/favourite$', views.favourite, name="favourite"),
]