#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yuchou
@time: 2017/8/3 16:22
"""
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)$', views.detail, name='detail'),
]