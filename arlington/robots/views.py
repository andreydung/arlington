from django.views.generic import TemplateView


class RobotsView(TemplateView):
    template_name = 'robots/robots.txt'
    content_type = 'text/plain'

robots = RobotsView.as_view()
