from django.conf.urls import url, include

import views

from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/$', login, kwargs={'template_name': 'upload/account/login.html'}, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': '/'}, name='logout'),

    #url(r'^login/', views.login, name='login'),

    url(r'^cloud/$', views.cloud, name='cloud'),

    url(r'^upload/', views.upload, name='upload'),
    url(r'^file/(?P<file_id>[A-Za-z0-9_.]+)/$', views.file, name='file')
]
