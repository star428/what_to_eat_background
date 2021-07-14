#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: urls.py
@time: 2021/7/12 21:12
@desc:
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views

app_name = 'polls'   # 重点是这一行

urlpatterns = [

    path('', views.index, name='index'),
# 例如: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # 例如: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # 例如: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('login/', views.login, name='login'),

    path('api-auth/', include('rest_framework.urls')),
]

