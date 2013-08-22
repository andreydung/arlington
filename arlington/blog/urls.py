from django.conf.urls import patterns, include, url


urlpatterns = patterns('blog.views',

    # Post detail
    url(r'^(?P<slug>[-\w]+)/$',
        view='post_detail',
        name='post_detail'
    ),

    # Post list
    url(r'^$',
        view='post_list',
        name='post_list'
    ),

)
