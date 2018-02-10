from django.contrib import admin

# Register your models here.
from .models import Post
#model admin options
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","published_Date"]
    #list_display_links = ["updated"]

    list_filter = ["published_Date"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)
