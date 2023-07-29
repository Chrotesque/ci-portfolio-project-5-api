from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task


class Comment(models.Model):
    """
    Comment model for Tasks
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        task_cat = self.task.category if self.task.category else "No Category"
        task_title = self.task.title if self.task.title else self.task.body
        return f'({task_cat}) {task_title}: {self.body}'
