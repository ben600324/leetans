from django.contrib import admin
from .models import Post, Recipe, Carousel, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date_posted", "author"]
    search_fields = ('title', 'content')
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Recipe)
admin.site.register(Carousel)
admin.site.register(Contact)