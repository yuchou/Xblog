#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yuchou
@time: 2017/8/7 16:36
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']