from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"title : {self.title}"

    def get_absolute_url(self):
        return reverse('todo:detail',kwargs={'pk' : self.pk})
