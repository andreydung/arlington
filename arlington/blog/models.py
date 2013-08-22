from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic

from . import managers
from tags.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    published = models.DateTimeField(default=timezone.now, help_text=_('Future dates will not make post public.'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ['-published']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.post_detail', args=[str(self.slug)])

    def get_previous_post(self):
        return self.get_previous_by_published()

    def get_previous_post(self):
        return self.get_next_by_published()
