from django.db import models
from django.utils import timezone


class VisibilityManager(models.Manager):
    def is_public(self):
        return self.get_query_set().filter(public=True)

    def is_published(self):
        return self.get_query_set().filter(public=True, published__lte=timezone.now())

    def is_featured(self):
        return self.get_query_set().filter(public=True, published__lte=timezone.now(), featured=True)
