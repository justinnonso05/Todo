from django.urls import path
from . import views
from .views import TodoListView, CreateTodoView, UpdateTodoView, DeleteTodoView, UpdateProfileView, SearchResultView

# app_name ='tasks'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('tasks/add/', CreateTodoView.as_view(), name='add'),
    path('profile/<int:pk>/edit/', UpdateProfileView.as_view(), name='profile'),
    path('tasks/', TodoListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/edit/', UpdateTodoView.as_view(), name='edit'),
    path('tasks/<int:pk>/delete/', DeleteTodoView.as_view(), name='delete'),
    path('tasks/search/', SearchResultView.as_view(), name='search'),
]