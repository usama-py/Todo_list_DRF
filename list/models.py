from django.db import models
from django.contrib.auth.models import User


class ToDoItem(models.Model):
    # Choices for the status field
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of when the ToDoItem was created
    title = models.CharField(max_length=100, blank=True)  # Title of the ToDoItem
    description = models.TextField(max_length=1000, blank=True)  # Description of the ToDoItem
    due_date = models.DateField(null=True, blank=True)  # Due date of the ToDoItem
    tags = models.ManyToManyField('Tag', blank=True, null=True)  # Tags associated with the ToDoItem
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN',
        blank=True
    )  # Status of the ToDoItem
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who owns the ToDoItem

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)  # Name of the tag
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who owns the tag

    def __str__(self):
        return self.name
