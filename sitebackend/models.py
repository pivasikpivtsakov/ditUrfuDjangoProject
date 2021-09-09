from django.db import models


# Create your models here.

class DirectionGroup(models.Model):
    code = models.IntegerField()
    name = models.TextField()


class Direction(models.Model):
    code = models.IntegerField()
    name = models.TextField()
    group = models.ForeignKey(DirectionGroup, related_name='directions', on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)
