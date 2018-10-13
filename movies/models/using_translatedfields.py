from django.db import models
from translated_fields import TranslatedField


class TranslatedFieldsMovie(models.Model):
    year = models.IntegerField()
    title = TranslatedField(models.CharField("Title", max_length=190))
