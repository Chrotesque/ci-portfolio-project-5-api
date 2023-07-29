from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Category model which can be nested
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.parent} > {self.name}' if self.parent else f'{self.name}'
