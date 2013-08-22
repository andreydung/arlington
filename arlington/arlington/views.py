from django.views.generic import ListView
from django.shortcuts import render

from activity.models import ActivityItem


class HomeView(ListView):
    model = ActivityItem
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)

    #     item_list = []
    #     for item in self.object_list:
    #         if item.content_object.is_published:
    #             item_list.append(item)

    #     context['item_list'] = item_list
    #     return context

home = HomeView.as_view()


def server_error(request):
    return render(request, '500.html')
