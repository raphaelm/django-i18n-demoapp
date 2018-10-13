from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from movies.models import ModeltranslationMovie


@register(ModeltranslationMovie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title',)
