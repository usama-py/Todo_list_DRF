from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import *
from django.contrib.auth.models import User


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Save the user and create a token for authentication
        user = serializer.save()
        Token.objects.create(user=user)


class ToDoItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ToDoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retrieve the ToDoItems for the authenticated user
        user = self.request.user
        return ToDoItem.objects.filter(user=user)

    def perform_create(self, serializer):
        # Set the authenticated user as the owner of the ToDoItem
        serializer.save(user=self.request.user)


class ToDoItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retrieve the ToDoItems for the authenticated user
        user = self.request.user
        return ToDoItem.objects.filter(user=user)

    def perform_update(self, serializer):
        # Check if the user has permission to update the ToDoItem
        instance = serializer.save()
        if instance.user != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to update this ToDoItem.")

    def perform_destroy(self, instance):
        # Check if the user has permission to delete the ToDoItem
        if instance.user != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to delete this ToDoItem.")
        instance.delete()
