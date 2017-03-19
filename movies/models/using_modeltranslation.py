from django.db import models


class ModeltransMovie(models.Model):
    title = models.CharField(max_length=190)
