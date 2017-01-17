from django.conf.urls import url, include
from . import views
app_name='homepage'
urlpatterns = [

     url(r'^$', views.homepage, name='homepage')
]
