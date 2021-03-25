from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ['body', 'title', 'slug', 'image', 'image2', 'image3',  'price', 'currency']


admin.site.register(Post, PostAdmin)
