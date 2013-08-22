from django.conf.urls import patterns, include, url


urlpatterns = patterns('robots.views',

    url(r'^$',
        view='robots',
        name='robots'
    ),

)
