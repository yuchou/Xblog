#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yuchou
@time: 2017/8/3 16:22
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]