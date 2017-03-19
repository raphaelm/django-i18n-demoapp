from django.db import models
from parler.models import TranslatedFields, TranslatableModel


class ParlerMovie(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField("Title", max_length=190)
    )
