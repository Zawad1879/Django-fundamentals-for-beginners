from django.conf.urls import url, include
from . import views
app_name = 'post'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^posts/$',views.post_list, name='post_list'),
    url(r'^(?P<post_id>[0-9]+)/$', views.delete, name='delete')
]
