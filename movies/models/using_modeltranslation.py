from django.db import models


class ModeltransMovie(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=190)
