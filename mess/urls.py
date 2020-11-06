from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from mess import views

urlpatterns =format_suffix_patterns( [
    path('login',views.login),#login a user
    path('signup',views.signup),#singnup a user
    path('all',views.mess_list),#login a user
    path('<int:mess_id>',views.mess_detail),#singnup a user
    path('user/<int:user_id>',views.fromview),#login a user
    path('mess/<int:mess_id>',views.toview),#singnup a user
    path('<int:cancel_id>',views.appoint),#singnup a user
    path('add',views.add)

])# -*- coding: utf-8 -*-

