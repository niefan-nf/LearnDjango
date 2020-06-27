# !/usr/bin/env python  
# -*- coding:utf-8 -*-
# author: Fan
# create time: 2020/6/25 14:56
# file: urls.py
# description:

from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
