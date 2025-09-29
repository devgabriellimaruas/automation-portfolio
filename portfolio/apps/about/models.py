# apps/about/models.py
from django.db import models

class Tools(models.Model):
    name = models.CharField(max_length=80)
    order = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.order is None:
            last_tool = Tools.objects.order_by('-order').first()
            self.order = (last_tool.order + 1) if last_tool else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
