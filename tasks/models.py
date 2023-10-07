from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from categories.models import Category


class Task(models.Model):
    """ Task model to later contain comments and categories """
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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False,
                                    null=True, blank=True)
    state = models.CharField(max_length=3, choices=STATE_CHOICES,
                             default='NEW')
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES,
                                default='LO')
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    overdue = models.BooleanField(default=False)
    coowner = models.ManyToManyField(User, related_name='task_coowner',
                                     blank=True)

    class Meta:
        """ Sorting rule for tasks """
        ordering = ['-created_at']

    def __str__(self):
        """ Returns task title/body, accomodates missing category """
        task_cat = self.category if self.category else "No Category"
        task_title = self.title if self.title else self.body
        return f'({task_cat}): {task_title}'
