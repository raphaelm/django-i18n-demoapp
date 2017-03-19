from django.db import models
from i18nfield.fields import I18nCharField


class I18nFieldMovie(models.Model):
    year = models.IntegerField()
    title = I18nCharField(max_length=190)
