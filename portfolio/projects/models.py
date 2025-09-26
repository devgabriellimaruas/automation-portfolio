from django.db import models
import os
from django.conf import settings
from subprocess import run

class Project(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    video = models.FileField(upload_to='static/uploads')
    thumbnail = models.ImageField(upload_to='static/uploads')
    tags = models.CharField(max_length=300)
    link_project = models.URLField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name