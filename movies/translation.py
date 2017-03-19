from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from movies.models import ModeltransMovie


@register(ModeltransMovie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title',)
