from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Task model containing user created categories and pre-defined states and priority settings
    """

    STATE_CHOICES = [
        ('NEW', 'New'),
        ('WIP', 'Work in Progress'),
        ('DEL', 'Delayed'),
        ('DON', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('LO', 'Low'),
        ('MI', 'Medium'),
        ('HI', 'High'),
        ('CR', 'Critical'),
    ]

    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default='NEW')
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='LO')
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    overdue = models.BooleanField(default=False)
    coowner = models.ManyToManyField(User, related_name='task_coowner', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
