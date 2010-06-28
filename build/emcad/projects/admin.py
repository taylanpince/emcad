from django.contrib import admin

from projects.models import Category, Project, Photo


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "order")
    search_fields = ("title", "slug", "blurb")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug", "order"), "blurb", "image"),
        }),
    )


class PhotoAdmin(admin.StackedInline):
    model = Photo


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "category", "order")
    list_filter = ("category", )
    search_fields = ("title", "subtitle", "blurb", "content")
    save_on_top = True
    inlines = [
        PhotoAdmin,
    ]
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug", "order"), "subtitle", "category", "blurb", "image", "content"),
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
