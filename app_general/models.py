from django.db import models

# Create your models here.

class TaskModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    finished = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name