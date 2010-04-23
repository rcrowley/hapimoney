from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    # Example:
    # (r"^hapimoney/", include("hapimoney.foo.urls")),

    # Static pages.
    url(r"^$", "hapimoney.base.views.index", name="index"),
    url(r"^process/?$", "hapimoney.base.views.process", name="process"),
    url(r"^about/?$", "hapimoney.base.views.about", name="about"),

    # Login and logout.
    url(r"^login/?$", "django.contrib.auth.views.login", name="login"),
    url(r"^logout/?$", "django.contrib.auth.views.logout", name="logout"),
    # TODO Sign up.
    # TODO Password reset and change.

    # The actual HapiMoney application.
    url(r"^basic/?$", "hapimoney.base.views.basic", name="basic"),
    url(r"^budget/?$", "hapimoney.base.views.budget", name="budget"),
    url(r"^balancesheet/?$", "hapimoney.base.views.balancesheet",
        name="balancesheet"),
    url(r"^risk/?$", "hapimoney.base.views.risk", name="risk"),
    url(r"^report/?$", "hapimoney.base.views.report", name="report"),

    # Uncomment the admin/doc line below and add "django.contrib.admindocs" 
    # to INSTALLED_APPS to enable admin documentation:
    # (r"^admin/doc/", include("django.contrib.admindocs.urls")),

    # Uncomment the next line to enable the admin:
    (r"^admin/", include(admin.site.urls)),
)
