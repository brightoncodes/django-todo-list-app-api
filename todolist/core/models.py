from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"title : {self.title}"
