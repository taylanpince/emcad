from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Admin
    (r'^admin/', include(admin.site.urls)),
    
    # Projects
    (r'^projects/', include('projects.urls')),
)

urlpatterns += patterns('django.views.generic.simple',
    # Home
    url(r"^$", "direct_to_template", {
        "template": "home.html",
    }, name="home"),

    # Why EMCAD
    url(r"^why-emcad/$", "direct_to_template", {
        "template": "why/emcad.html",
    }, name="why_emcad"),
    url(r"^why-emcad/leed/$", "direct_to_template", {
        "template": "why/leed.html",
    }, name="why_emcad_leed"),
    url(r"^why-emcad/go-green/$", "direct_to_template", {
        "template": "why/go-green.html",
    }, name="why_emcad_green"),

    # Who We Are
    url(r"^who-we-are/$", "direct_to_template", {
        "template": "who/dave-myles.html",
    }, name="who_dave_myles"),
    url(r"^who-we-are/project-team/$", "direct_to_template", {
        "template": "who/project-team.html",
    }, name="who_project_team"),
    url(r"^who-we-are/giving-back/$", "direct_to_template", {
        "template": "who/giving-back.html",
    }, name="who_giving_back"),

    # Services
    url(r"^services/$", "direct_to_template", {
        "template": "services.html",
    }, name="services"),

    # Contact
    url(r"^contact/$", "direct_to_template", {
        "template": "contact.html",
    }, name="contact"),

    # Careers
    url(r"^careers/$", "direct_to_template", {
        "template": "careers.html",
    }, name="careers"),

    # Blog
    url(r"^blog/$", "direct_to_template", {
        "template": "blog.html",
    }, name="blog"),
)
