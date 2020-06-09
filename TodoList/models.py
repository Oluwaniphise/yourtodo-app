from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now, blank=True)
    def __str__(self):
        return self.title
