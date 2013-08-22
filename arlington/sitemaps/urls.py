from django.conf.urls import patterns, url, include
from django.contrib.sitemaps import GenericSitemap, FlatPageSitemap

from blog.models import Post


# link_dict = {
#     'queryset': Link.objects.is_published(),
#     'date_field': 'modified',
# }

# photo_dict = {
#     'queryset': Photo.objects.is_published(),
#     'date_field': 'modified',
# }

# video_dict = {
#     'queryset': Video.objects.is_published(),
#     'date_field': 'modified',
# }

post_dict = {
    'queryset': Post.objects.is_published(),
    'date_field': 'updated',
}

# project_dict = {
#     'queryset': Project.objects.is_published(),
#     'date_field': 'modified',
# }


sitemaps = {
    # 'link': GenericSitemap(link_dict, priority=0.5),
    # 'photo': GenericSitemap(photo_dict, priority=0.5),
    # 'video': GenericSitemap(video_dict, priority=0.5),
    'post': GenericSitemap(post_dict, priority=0.5),
    # 'project': GenericSitemap(project_dict, priority=0.5),
    'flatpages': FlatPageSitemap,
}

# sitemaps_photos = {
#     'photo': GenericSitemap(photo_dict, priority=0.5),
# }

# sitemaps_videos = {
#     'video': GenericSitemap(video_dict, priority=0.5),
# }

sitemaps_sections = {
    # 'link': GenericSitemap(link_dict, priority=0.5),
    'post': GenericSitemap(post_dict, priority=0.5),
    # 'project': GenericSitemap(project_dict, priority=0.5),
    'flatpages': FlatPageSitemap,
}

urlpatterns = patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$','index', {'sitemaps': sitemaps}),
    # (r'^sitemap-photo.xml$', 'sitemap', {'sitemaps': sitemaps_photos, 'template_name': 'sitemaps/photos.html'}),
    # (r'^sitemap-video.xml$', 'sitemap', {'sitemaps': sitemaps_videos, 'template_name': 'sitemaps/videos.html'}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps_sections}),
)
