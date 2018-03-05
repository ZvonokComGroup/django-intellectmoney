# -*- coding: utf-8 -*-
try:
    from django.conf.urls import url, include
except ImportError:
    from django.urls import re_path as url, include
from intellectmoney import views

urlpatterns = [
    url(r'^result/$', views.receive_result, name='intellectmoney-result'),
    url(r'^success/result/$', views.success, name='intellectmoney-success'),
    url(r'^fail/result/$', views.fail, name='intellectmoney-fail'),
]
