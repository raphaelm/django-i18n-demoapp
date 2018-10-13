from django.contrib import admin
from django.forms import ModelForm
from hvad.admin import TranslatableAdmin as HvadTranslatableAdmin
from i18nfield import forms
from modeltranslation.admin import TranslationAdmin as MTranslationAdmin
from parler.admin import TranslatableAdmin as ParlerTranslatableAdmin
from translated_fields import TranslatedFieldAdmin

from movies.models import ParlerMovie, HvadMovie, NeceMovie, ModeltranslationMovie, ModeltransMovie, \
    TranslatedFieldsMovie, I18nFieldMovie, ClassicMovie


class ParlerAdmin(ParlerTranslatableAdmin):
    list_display = ('title',)


class HvadAdmin(HvadTranslatableAdmin):
    pass


class ModeltranslationAdmin(MTranslationAdmin):
    pass


class ModeltransAdmin(admin.ModelAdmin):
    pass


class MTranslatedFieldAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    pass


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
admin.site.register(ModeltranslationMovie, ModeltranslationAdmin)
admin.site.register(ModeltransMovie, ModeltransAdmin)
admin.site.register(TranslatedFieldsMovie, MTranslatedFieldAdmin)
admin.site.register(I18nFieldMovie, I18nFieldAdmin)
