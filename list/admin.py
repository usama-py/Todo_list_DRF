from django.contrib import admin
from .models import ToDoItem, Tag

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'user')  # Displayed fields in the admin list view
    list_filter = ('status', 'user')  # Filter options in the admin list view
    search_fields = ('title', 'user__username')  # Fields used for searching in the admin list view

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')  # Displayed fields in the admin list view
    list_filter = ('user',)  # Filter options in the admin list view
    search_fields = ('name', 'user__username')  # Fields used for searching in the admin list view
