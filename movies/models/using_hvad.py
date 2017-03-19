from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


class HvadMovie(TranslatableModel):
    year = models.IntegerField()
    translations = TranslatedFields(
        title=models.CharField(max_length=190),
    )
