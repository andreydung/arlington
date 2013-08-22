from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string
from django.db.models.signals import post_save

from blog.models import Post


class ActivityItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    @property
    def title(self):
        return self.content_object.title

    @property
    def tags(self):
        return self.content_object.tags.all()

    def get_absolute_url(self):
        return self.content_object.get_absolute_url()

    def render_full(self):
        template_name = 'activity/activityitem_full_%s.html' % (self.content_type.name)
        return render_to_string(template_name, {'object': self.content_object})

    def render_preview(self):
        template_name = 'activity/activityitem_preview_%s.html' % (self.content_type.name)
        return render_to_string(template_name, {'object': self.content_object})


def create_activity_item(sender, **kwargs):
    if 'created' in kwargs:
        if kwargs['created']:
            instance = kwargs['instance']
            content_type = ContentType.objects.get_for_model(instance)
            object_id = instance.id
            activity_item = ActivityItem.objects.create(content_type=content_type, object_id=object_id)


post_save.connect(create_activity_item, sender=Post)
