from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

urlpatterns =format_suffix_patterns( [

    path('user/post',views.user_post_view),#posting a user post
    path('user/<int:pk>',views.user_post_detail),#geeting a specific user post
    path('club/post',views.club_post_view),#posting a club
    path('club/<int:pk>',views.club_post_detail),#getting  specific club post
    
    path('userspecific/<int:user_id>',views.UserSpecificPost),
    path('clubspecific/<int:club_id>',views.ClubSpecificPost),
    path('user/student/all',views.UserStudentPost),#post for all students
    path('user/prof/all',views.UserProfPost),#post for all professors
    path('club/student/all',views.ClubStudentPost),
    path('club/prof/all',views.ClubProfPost),
    path('user/student/<int:dept_id>',views.DeptSpecificStudentUserPost),#dept specific post
    path('club/student/<int:dept_id>',views.DeptSpecificStudentClubPost),#dept specific post
    path('user/prof/<int:dept_id>',views.DeptSpecificStudentClubPost),#dept specific post
    path('club/prof/<int:dept_id>',views.DeptSpecificProfClubPost),#dept specific post
    # path('club/student/<int:dept_id>/<int:club_id'),
    # path('club/prof/<int:dept_id>/<int:club_id')
 
])