from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


class HvadMovie(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=190),
    )
