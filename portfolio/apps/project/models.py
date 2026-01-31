from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    tools = models.CharField(max_length=300)
    link_project = models.URLField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name