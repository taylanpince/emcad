from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """
    A project category
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    blurb = models.TextField(_("Blurb"), blank=True)
    image = models.ImageField(_("Image"), upload_to="files/projects/categories", blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ("projects_category", (), {
            "category_slug": self.slug,
        })

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __unicode__(self):
        return self.title


class Project(models.Model):
    """
    A project, tied to a category
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    blurb = models.TextField(_("Blurb"), blank=True)
    content = models.TextField(_("Content"), blank=True)
    image = models.ImageField(_("Image"), upload_to="files/projects/categories", blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("Category"), related_name="projects")

    @models.permalink
    def get_absolute_url(self):
        return ("projects_project", (), {
            "category_slug": self.category.slug,
            "project_slug": self.slug,
        })

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __unicode__(self):
        return self.title
