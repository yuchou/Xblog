#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yuchou
@time: 2017/8/7 16:57
"""
from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]