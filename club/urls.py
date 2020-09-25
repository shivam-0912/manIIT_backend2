from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from club import views

urlpatterns =format_suffix_patterns( [

    path('<int:pk>',views.club_detail),#getting club info
    path('user/<int:pk>',views.club_user_detail)#for getting club_id from user_id
 
])# -*- coding: utf-8 -*-

