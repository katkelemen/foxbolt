from django.db import models

# Create your models here.

class Item (models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name