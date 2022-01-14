from django.db import models
from django.contrib.auth.models import User

from api.constants import TodoStatus


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=12,
                              choices=TodoStatus.choices, default=TodoStatus.TODO)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified']
