from django.urls import path,include
from . import views

urlpatterns = [
    path('profile-list/',views.profile_list,name='profile-list'),
    path('profile-detail/<int:pk>/',views.profile_detail,name='api-profile-detail'),
]
