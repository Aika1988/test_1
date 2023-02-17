from django.contrib import admin
from .models import *


class ImageAdminInline(admin.TabularInline):
    model = PostImage
    max_num = 20
    min_num = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageAdminInline,]


admin.site.register(Category)


