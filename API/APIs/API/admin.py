from django.contrib import admin
from . import models

class FeedItemAdmin(admin.ModelAdmin): list_display = ('id', 'title', 'url')
admin.site.register(models.FeedItem, FeedItemAdmin)
