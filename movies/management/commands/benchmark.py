import timeit

from django.core import cache
from django.core.management.base import BaseCommand
from django.utils import translation
from faker import Faker
from i18nfield.strings import LazyI18nString

from movies.models import HvadMovie, ParlerMovie, NeceMovie, ModeltransMovie, I18nFieldMovie, KlingonMovie


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
""", globals=globals(), number=Nruns)/Nruns)

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
""", globals=globals(), number=Nruns)/Nruns)

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
""", globals=globals(), number=Nruns)/Nruns)

        ModeltransMovie.objects.all().delete()
        for i in range(N):
            ModeltransMovie.objects.create(
                title_en=fake.text(max_nb_chars=140),
                title_it='it' + fake_it.text(max_nb_chars=140),
                year=fake.year()
            )

        print("Modeltrans", timeit.timeit("""
for m in ModeltransMovie.objects.all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=1))
        print("Modeltrans", timeit.timeit("""
for m in ModeltransMovie.objects.all():
    if not str(m.title).startswith('it'):
        raise ValueError(m.title)
""", globals=globals(), number=Nruns)/Nruns)

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
""", globals=globals(), number=Nruns)/Nruns)

        KlingonMovie.objects.all().delete()
        for i in range(N):
            movie = KlingonMovie.objects.create(
                title=fake.text(max_nb_chars=140),
                year=2009
            )
            movie.set_translation('it', 'title', 'it' + fake_it.text(max_nb_chars=140))

        print("Klingon", timeit.timeit("""
for m in KlingonMovie.objects.all():
    if not str(m.get_translation('it', 'title')).startswith('it'):
        raise ValueError(m)
""", globals=globals(), number=1))
        print("Klingon", timeit.timeit("""
for m in KlingonMovie.objects.all():
    if not str(m.get_translation('it', 'title')).startswith('it'):
        raise ValueError(m)
""", globals=globals(), number=Nruns)/Nruns)
