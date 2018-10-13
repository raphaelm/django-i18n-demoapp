# Create your views here.
import hvad.forms
import parler.forms
from django import forms
from django.shortcuts import render
from django.utils.translation import override

from movies.models import ParlerMovie, HvadMovie, ModeltranslationMovie, TranslatedFieldsMovie, I18nFieldMovie, \
    ModeltransMovie


class ParlerForm(parler.forms.TranslatableModelForm):
    title = parler.forms.TranslatedField()

    class Meta:
        model = ParlerMovie
        fields = ['title', 'year']


class HvadForm(hvad.forms.TranslatableModelForm):
    class Meta:
        model = HvadMovie
        fields = ['title', 'year']


class ModeltranslationForm(forms.ModelForm):
    class Meta:
        model = ModeltranslationMovie
        fields = ['title', 'title_it', 'year']


class TranslatedFieldForm(forms.ModelForm):
    class Meta:
        model = TranslatedFieldsMovie
        fields = ['title_en', 'title_de', 'title_it', 'year']


class ModeltransForm(forms.ModelForm):
    class Meta:
        model = ModeltransMovie
        fields = ['title', 'title_it', 'year']


class I18nFieldForm(forms.ModelForm):
    class Meta:
        model = I18nFieldMovie
        fields = ['title', 'year']


def forms(request, lng):
    with override(lng):
        return render(request, 'forms.html', {
            'parler_form': ParlerForm(instance=ParlerMovie.objects.first()),
            'hvad_form': HvadForm(instance=HvadMovie.objects.first()),
            'modeltranslation_form': ModeltranslationForm(instance=ModeltranslationMovie.objects.first()),
            'modeltrans_form': ModeltransForm(instance=ModeltransMovie.objects.first()),
            'translatedfields_form': TranslatedFieldForm(instance=TranslatedFieldsMovie.objects.first()),
            'i18nfield_form': I18nFieldForm(instance=I18nFieldMovie.objects.first()),
        })
