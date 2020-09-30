from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from appointment import views

urlpatterns =format_suffix_patterns( [

    path('from/<int:user_id>',views.fromview),#login a user
    path('to/<int:user_id>',views.toview),#singnup a user
    path('<int:appointment_id>',views.appoint),#singnup a user
    path('add',views.add)
 
])# -*- coding: utf-8 -*-

