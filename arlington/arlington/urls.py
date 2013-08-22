from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Blog
    url(r'^blog/', include('blog.urls')),

    # Tags
    url(r'^tags/', include('tags.urls')),

    # Sitemaps
    url(r'^', include('sitemaps.urls')),

    # Robots
    url(r'^robots.txt$', include('robots.urls')),

    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Home
    url(r'^$', 'arlington.views.home', name='home'),

    # About
    url(r'^about/$', 'django.contrib.flatpages.views.flatpage', {'url': '/about/'}, name='about'),

)

handler500 = 'arlington.views.server_error'
