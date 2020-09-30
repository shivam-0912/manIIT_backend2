from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from club_user import views

urlpatterns =format_suffix_patterns( [

    path('user/<int:user_id>',views.user_specific),#login a user
    path('club/<int:club_id>',views.club_specific),#login a user
    path('add',views.add),
    path('delete',views.delete)
 
])# -*- coding: utf-8 -*-

