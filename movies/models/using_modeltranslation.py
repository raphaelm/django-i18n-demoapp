from django.db import models


class ModeltranslationMovie(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=190)
