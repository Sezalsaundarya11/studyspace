from django.db import models
from django.contrib.auth.models import User
from Topic.models import Topic

# Create your models here.

    
class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # members
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-updated', '-created']
    




