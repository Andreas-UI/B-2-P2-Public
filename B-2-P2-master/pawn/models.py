from django.db import models

from .fields import PawnFormField


class PawnField(models.TextField):

    def formfield(self, **kwargs):

        defaults = {'form_class': PawnFormField}
        defaults.update(kwargs)
        return super(PawnField, self).formfield(**defaults)