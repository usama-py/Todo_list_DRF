from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),  # Endpoint for user creation
    path('todos/', ToDoItemListCreateView.as_view(), name='todo-list-create'),  # Endpoint for listing and creating ToDoItems
    path('todos/<int:pk>/', ToDoItemRetrieveUpdateDeleteView.as_view(), name='todo-retrieve-update-delete'),  # Endpoint for retrieving, updating, and deleting a specific ToDoItem
    path('login/', obtain_auth_token, name='token-auth'),  # Endpoint for obtaining authentication token
]
