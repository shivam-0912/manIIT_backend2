from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns =format_suffix_patterns( [

    path('login',views.login),#login a user
    path('signup',views.signup),#singnup a user
    path('prof/all',views.profall),#singnup a user
    path('user/<int:pk>',views.user_detail)#getting a specific user detail
 
])