from django.conf.urls.defaults import *


urlpatterns += patterns('projects.views',
    url(r"^$", "categories", name="projects_categories"),
    url(r"^(?P<category_slug>[-\w]+)/$", "category_detail", name="projects_category_detail"),
    url(r"^(?P<category_slug>[-\w]+)/(?P<project_slug>[-\w]+)/$", "project_detail", name="projects_project_detail"),
)
