from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from projects.models import Category, Project


def categories_list(request):
    """
    A list of categories
    """
    categories = Category.objects.all()

    return render_to_response("projects/categories.html", {
        "categories": categories,
    }, context_instance=RequestContext(request))


def category_detail(request, category_slug):
    """
    Category detail page
    """
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.all()

    return render_to_response("projects/category.html", {
        "category": category,
        "categories": categories,
    }, context_instance=RequestContext(request))


def project_detail(request, category_slug, project_slug):
    """
    Project detail page
    """
    project = get_object_or_404(Project, slug=project_slug)
    categories = Category.objects.all()

    return render_to_response("projects/project.html", {
        "project": project,
        "category": project.category,
        "categories": categories,
    }, context_instance=RequestContext(request))
