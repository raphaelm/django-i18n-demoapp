from django.db import models
from klingon.models import Translatable


class Book(models.Model, Translatable):
    title = models.CharField(max_length=190)
    translatable_fields = ('title',)
