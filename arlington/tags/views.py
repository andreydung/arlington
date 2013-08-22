from django.views.generic import ListView, DetailView

from .models import Tag
from activity.models import ActivityItem


class TagListView(ListView):
    model = Tag

tag_list = TagListView.as_view()


class TagDetailView(DetailView):
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)

        item_list = []
        for item in ActivityItem.objects.all():
            if self.object in item.tags:
                item_list.append(item)

        context['item_list'] = item_list
        return context

tag_detail = TagDetailView.as_view()
