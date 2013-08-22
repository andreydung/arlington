from django.template import RequestContext
from django.contrib.sites.models import Site

from django.conf import settings


def get_analytics(request):
    google_analytics_id = getattr(settings, 'GOOGLE_ANALYTICS_ID', '')

    return {
        'google_analytics_id': google_analytics_id
    }
