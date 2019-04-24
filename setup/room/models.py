from django.db import models
from django.forms import ModelForm

# Create your models here.
class FloorSize(models.Model):
    """docstring for FloorSize."""

    name = models.CharField(max_length=200)
    floor_length = models.PositiveIntegerField()
    floor_width = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class RoomForm(ModelForm):
    """docstring for RoomForm."""
    class Meta:
        model = FloorSize
        fields = '__all__'
