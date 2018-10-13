import timeit

from django.core import cache
from django.core.management.base import BaseCommand
from django.utils import translation
from faker import Faker
from i18nfield.strings import LazyI18nString

from movies.models import HvadMovie, ParlerMovie, NeceMovie, ModeltranslationMovie, I18nFieldMovie, \
    ModeltransMovie, TranslatedFieldsMovie


class Command(BaseCommand):
    help = 'CreateTestData'

    def handle(self, *args, **options):
        fake = Faker()
        fake_it = Faker(locale='it_IT')
        N = 1000
        Nruns = 10
        translation.activate('it')

        HvadMovie.objects.all().delete()
        for i in range(N):
            movie = HvadMovie.objects.language('en').create(
                title=fake.text(max_nb_chars=140),
                year=fake.year()
            )
            movie.translate('it')
            movie.title = 'it' + fake_it.text(max_nb_chars=140)
            movie.save()

        print("Hvad", timeit.timeit("""
for m in HvadMovie.objects.language('it').all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=1))
        print("Hvad", timeit.timeit("""
for m in HvadMovie.objects.language('it').all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=Nruns) / Nruns)

        ParlerMovie.objects.all().delete()
        for i in range(N):
            movie = ParlerMovie.objects.language('en').create(
                title=fake.text(max_nb_chars=140),
                year=fake.year()
            )
            movie.set_current_language('it')
            movie.title = 'it' + fake_it.text(max_nb_chars=140)
            movie.save()

        print("Parler", timeit.timeit("""
for m in ParlerMovie.objects.language('it').all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=1))
        print("Parler", timeit.timeit("""
for m in ParlerMovie.objects.language('it').all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=Nruns) / Nruns)

        NeceMovie.objects.all().delete()
        for i in range(N):
            movie = NeceMovie.objects.language('en').create(
                title=fake.text(max_nb_chars=140),
                year=fake.year()
            )
            movie.translate('it', title='it' + fake_it.text(max_nb_chars=140))
            movie.save()

        print("Nece", timeit.timeit("""
for m in NeceMovie.objects.language('it').all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=1))
        print("Nece", timeit.timeit("""
for m in NeceMovie.objects.language('it').all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=Nruns) / Nruns)

        ModeltranslationMovie.objects.all().delete()
        for i in range(N):
            ModeltranslationMovie.objects.create(
                title_en=fake.text(max_nb_chars=140),
                title_it='it' + fake_it.text(max_nb_chars=140),
                year=fake.year()
            )

        print("Modeltranslation", timeit.timeit("""
for m in ModeltranslationMovie.objects.all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=1))
        print("Modeltranslation", timeit.timeit("""
for m in ModeltranslationMovie.objects.all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=Nruns) / Nruns)

        I18nFieldMovie.objects.all().delete()
        for i in range(N):
            I18nFieldMovie.objects.create(
                title=LazyI18nString({
                    'it': 'it' + fake_it.text(max_nb_chars=140),
                    'en': fake.text(max_nb_chars=140),
                }),
                year=fake.year()
            )

        print("I18nField", timeit.timeit("""
for m in I18nFieldMovie.objects.all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=1))
        print("I18nField", timeit.timeit("""
for m in I18nFieldMovie.objects.all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=Nruns) / Nruns)

        ModeltransMovie.objects.all().delete()
        for i in range(N):
            movie = ModeltransMovie.objects.create(
                title=fake.text(max_nb_chars=140),
                year=2009
            )
            movie.title_it = 'it' + fake_it.text(max_nb_chars=140)
            movie.save()

        print("Modeltrans", timeit.timeit("""
for m in ModeltransMovie.objects.all():
    if not m.title_it.startswith('it'):
        raise ValueError(m)
""", globals=globals(), number=1))
        print("Modeltrans", timeit.timeit("""
for m in ModeltransMovie.objects.all():
    if not m.title_it.startswith('it'):
        raise ValueError(m)
""", globals=globals(), number=Nruns) / Nruns)

        TranslatedFieldsMovie.objects.all().delete()
        for i in range(N):
            movie = TranslatedFieldsMovie.objects.create(
                title_en=fake.text(max_nb_chars=140),
                title_it='it' + fake_it.text(max_nb_chars=140),
                year=2009
            )

        print("TranslatedFields", timeit.timeit("""
for m in TranslatedFieldsMovie.objects.all():
    if not m.title_it.startswith('it'):
        raise ValueError(m)
""", globals=globals(), number=1))
        print("TranslatedFields", timeit.timeit("""
for m in TranslatedFieldsMovie.objects.all():
    if not m.title_it.startswith('it'):
        raise ValueError(m)
""", globals=globals(), number=Nruns) / Nruns)
