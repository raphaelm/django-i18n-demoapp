from django.db import models


class ClassicMovie(models.Model):
    title = models.CharField(max_length=190)
    year = models.IntegerField()
