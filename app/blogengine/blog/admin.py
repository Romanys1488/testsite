from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(AttributeType)
admin.site.register(ItemAttributes)
admin.site.register(BoundTable)
# Register your models here.
