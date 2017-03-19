from django.db import models
from nece.models import TranslationModel


class NeceMovie(TranslationModel):
    title = models.CharField(max_length=190)

    class Meta:
        translatable_fields = ('title',)
