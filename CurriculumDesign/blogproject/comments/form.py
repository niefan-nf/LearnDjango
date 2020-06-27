# !/usr/bin/env python  
# -*- coding:utf-8 -*-
# author: Fan
# create time: 2020/6/25 14:18
# file: form.py
# description:

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
