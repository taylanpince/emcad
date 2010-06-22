from django.contrib import admin

from projects.models import Category, Project


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
