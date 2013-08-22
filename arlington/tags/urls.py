from django.conf.urls import patterns, include, url


urlpatterns = patterns('tags.views',

    # Tag detail
    url(r'^(?P<slug>[-\w]+)/$',
        view='tag_detail',
        name='tag_detail'
    ),

    # Tag list
    url(r'^$',
        view='tag_list',
        name='tag_list'
    ),

)
