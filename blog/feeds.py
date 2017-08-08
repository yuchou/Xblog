#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yuchou
@time: 2017/8/8 15:51
"""
from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    title = "Django 博客教程演示项目"
    link = "/"
    description = "Django博客教程演示项目测试文章"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body