from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from projects.models import Category, Project


def categories(request):
    """
    A list of categories
    """
    return render_to_response("projects/categories.html", {
        
    }, context_instance=RequestContext(request))


def category_detail(request, category_slug):
    """
    Category detail page
    """
    return render_to_response("projects/category.html", {
        
    }, context_instance=RequestContext(request))


def project_detail(request, category_slug, project_slug):
    """
    Project detail page
    """
    return render_to_response("projects/project.html", {
        
    }, context_instance=RequestContext(request))
