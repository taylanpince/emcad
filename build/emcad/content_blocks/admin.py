from django.contrib import admin

from content_blocks.models import ContentBlock


class ContentBlockAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContentBlock, ContentBlockAdmin)
