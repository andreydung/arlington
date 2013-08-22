from django.views.generic import ListView, DetailView
from django.contrib.contenttypes.models import ContentType

from activity.models import ActivityItem
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.is_published()

post_list = PostListView.as_view()


class PostDetailView(DetailView):
    queryset = Post.objects.is_published()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        content_type = ContentType.objects.get_for_model(self.object)
        context['item'] = ActivityItem.objects.get(content_type=content_type, object_id=self.object.id)
        return context

post_detail = PostDetailView.as_view()
