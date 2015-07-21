from django.db import models
from picklefield.fields import PickledObjectField
# Create your models here.


class Graph(models.Model):
    title = models.CharField(max_length=100)
    fitequation = PickledObjectField()
    image = models.CharField(max_length=50)  # Doesn't make sense to resave the image to the harddrive so I'll just store
    # The current local