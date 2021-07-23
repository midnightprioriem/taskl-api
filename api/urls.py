from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from api import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('tasks/', 
        views.TaskList.as_view(),
        name='task-list'),
    path('task/<int:pk>/',
        views.TaskDetail.as_view(),
        name = 'task-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('user/<int:pk>/',
        views.UserDetail.as_view(),
        name = 'user-detail'),
])