from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('users/', views.display_users, name='user_list'),
]
