from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blag/$', views.post_list, name='post_list'),
    url(r'', views.home, name="home"),
]

