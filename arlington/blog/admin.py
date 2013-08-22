from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('public',)
    filter_horizontal = ('tags',)


admin.site.register(Post, PostAdmin)
