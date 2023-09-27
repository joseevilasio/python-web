from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "date"]
    list_filter = ["published", "date"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["-date"]


admin.site.register(Post, PostAdmin)
