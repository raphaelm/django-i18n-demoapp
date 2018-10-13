from django.db import models
from modeltrans.fields import TranslationField


class ModeltransMovie(models.Model):
    year = models.IntegerField()
    title = models.CharField("Title", max_length=190)
    i18n = TranslationField(fields=("title",))
