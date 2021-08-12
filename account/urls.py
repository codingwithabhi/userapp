
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login_user,name='login'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup_user,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('profile-detail/<int:pk>/',views.profile_detail,name='profile-detail'),
    path('profile-update/<int:pk>/',views.profile_update,name='profile-update'),
    
]
