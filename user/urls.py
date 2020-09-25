from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns =format_suffix_patterns( [

    path('login',views.login),
    path('signup',views.signup),
    path('user/<int:pk>',views.user_detail)
 
])