from django.core.management.base import BaseCommand
from i18nfield.strings import LazyI18nString

from movies.models import HvadMovie, ParlerMovie, NeceMovie, ModeltransMovie, I18nFieldMovie, KlingonMovie


class Command(BaseCommand):
    help = 'CreateTestData'

    def handle(self, *args, **options):
        HvadMovie.objects.all().delete()
        movie = HvadMovie.objects.language('en').create(
            title='Angels and Daemons',
            year=2009
        )
        movie.translate('it')
        movie.title = 'Angeli e demoni'
        movie.save()

        ParlerMovie.objects.all().delete()
        movie = ParlerMovie.objects.language('en').create(
            title='Angels and Daemons',
            year=2009
        )
        movie.set_current_language('it')
        movie.title = 'Angeli e demoni'
        movie.save()

        NeceMovie.objects.all().delete()
        movie = NeceMovie.objects.language('en').create(
            title='Angels and Daemons',
            year=2009
        )
        movie.translate('it', title='Angeli e demoni')
        movie.save()

        ModeltransMovie.objects.all().delete()
        ModeltransMovie.objects.create(
            title_en='Angels and Daemons',
            title_it='Angeli e demoni',
            year=2009
        )

        I18nFieldMovie.objects.all().delete()
        I18nFieldMovie.objects.create(
            title=LazyI18nString({
                'it': 'Angeli e demoni',
                'en': 'Angels and Daemons'
            }),
            year=2009
        )

        KlingonMovie.objects.all().delete()
        movie = KlingonMovie.objects.create(
            title="Angels and Daemons",
            year=2009
        )
        movie.set_translation('it', 'title', 'Angeli e demoni')
