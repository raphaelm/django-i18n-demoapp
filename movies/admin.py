from django.contrib import admin
from django.forms import ModelForm, TextInput
from i18nfield import forms
from klingon.admin import TranslationInline, TranslationInlineForm
from modeltranslation.admin import TranslationAdmin as MTranslationAdmin
from parler.admin import TranslatableAdmin as ParlerTranslatableAdmin
from hvad.admin import TranslatableAdmin as HvadTranslatableAdmin

from movies.models import ParlerMovie, HvadMovie, NeceMovie, ModeltransMovie, KlingonMovie, I18nFieldMovie, ClassicMovie


class ParlerAdmin(ParlerTranslatableAdmin):
    list_display = ('title',)


class HvadAdmin(HvadTranslatableAdmin):
    pass


class ModeltransAdmin(MTranslationAdmin):
    pass


class RichTranslationInlineForm(TranslationInlineForm):
    widgets = {
        'title': TextInput(attrs={'class': 'klingon-char-field'}),
    }


class RichTranslationInline(TranslationInline):
    form = RichTranslationInlineForm


class KlingonAdmin(admin.ModelAdmin):
    inlines = [RichTranslationInline]


class I18nFieldForm(ModelForm):
    class Meta:
        model = I18nFieldMovie
        fields = ['title', 'year']
        widgets = {
            'title': forms.I18nTextInput,
            'abstract': forms.I18nTextarea
        }


class I18nFieldAdmin(admin.ModelAdmin):
    form = I18nFieldForm

admin.site.register(ParlerMovie, ParlerAdmin)
admin.site.register(HvadMovie, HvadAdmin)
admin.site.register(NeceMovie)
admin.site.register(ClassicMovie)
admin.site.register(ModeltransMovie, ModeltransAdmin)
admin.site.register(KlingonMovie, KlingonAdmin)
admin.site.register(I18nFieldMovie, I18nFieldAdmin)

