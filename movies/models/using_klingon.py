from django.db import models
from klingon.models import Translatable


class KlingonMovie(models.Model, Translatable):
    year = models.IntegerField()
    title = models.CharField(max_length=190)
    translatable_fields = ('title',)
