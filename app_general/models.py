from django.db import models

# Create your models here.

class TaskModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    finished = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.id)
        
class LikeModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class FriendModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    like = models.ManyToManyField(LikeModel)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return str(self.id)