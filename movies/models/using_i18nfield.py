from django.db import models
from i18nfield.fields import I18nCharField
from nece.models import TranslationModel


class I18nFieldMovie(TranslationModel):
    title = I18nCharField(max_length=190)
