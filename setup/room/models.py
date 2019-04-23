from django.db import models

# Create your models here.
class FloorSize(models.Model):
    """docstring for FloorSize."""

    name = models.CharField(max_length=200)
    floor_length = models.PositiveIntegerField()
    floor_width = models.PositiveIntegerField()

    def __str__(self):
        return self.name
