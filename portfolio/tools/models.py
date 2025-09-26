from django.db import models

# Create your models here.
class Tools(models.Model):
    name = models.CharField(max_length=80, unique=True)
    order = models.IntegerField()
    
    def __str__(self):
        return self.name