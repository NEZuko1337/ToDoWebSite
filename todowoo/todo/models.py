from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, max_length=512)
    importance = models.BooleanField(default= False)
    date = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null = True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Свзять пользователей и его записей

    def __str__(self):
        return self.title


