from datetime import datetime
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=32, blank=False)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title