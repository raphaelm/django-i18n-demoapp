# Create your views here.
import parler.forms
import hvad.forms
from django import forms
from django.shortcuts import render
from django.utils.translation import override

from movies.models import ParlerMovie, HvadMovie, ModeltransMovie, KlingonMovie, I18nFieldMovie


class ParlerForm(parler.forms.TranslatableModelForm):
    title = parler.forms.TranslatedField()

    class Meta:
        model = ParlerMovie
        fields = ['title', 'year']


class HvadForm(hvad.forms.TranslatableModelForm):
    class Meta:
        model = HvadMovie
        fields = ['title', 'year']


class ModeltransForm(forms.ModelForm):
    class Meta:
        model = ModeltransMovie
        fields = ['title', 'title_it', 'year']


class KlingonForm(forms.ModelForm):
    class Meta:
        model = KlingonMovie
        fields = ['title', 'year']


class I18nFieldForm(forms.ModelForm):
    class Meta:
        model = I18nFieldMovie
        fields = ['title', 'year']


def forms(request, lng):
    with override(lng):
        return render(request, 'forms.html', {
            'parler_form': ParlerForm(instance=ParlerMovie.objects.first()),
            'hvad_form': HvadForm(instance=HvadMovie.objects.first()),
            'modeltrans_form': ModeltransForm(instance=ModeltransMovie.objects.first()),
            'klingon_form': KlingonForm(instance=KlingonMovie.objects.first()),
            'i18nfield_form': I18nFieldForm(instance=I18nFieldMovie.objects.first()),
        })
