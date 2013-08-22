from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import post_save


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('tags.views.tag_detail', args=[str(self.slug)])

    def render_full(self):
        template_name = 'activity/activityitem_full_%s.html' % (self.content_type.name)
        return render_to_string(template_name, {'object': self.content_object})

    def render_preview(self):
        template_name = 'activity/activityitem_preview_%s.html' % (self.content_type.name)
        return render_to_string(template_name, {'object': self.content_object})
