from django.contrib import admin
from . import models

# Register your models here.

class CommentTabularInline(admin.TabularInline):
    model = models.Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentTabularInline]
    class Meta:
        model = models.Post

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Like)