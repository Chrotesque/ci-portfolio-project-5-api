from django.db import models


class Category(models.Model):
    """
    Category model which can be nested
    """
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = "Categories"

    def __str__(self):
        # no parent assigned
        if not self.parent:
            return f'{self.name}'
        # parent has been assigned
        else:
            return f'{self.parent} > {self.name}'

