
After header, add homepage_block to accomondate home banner page, add a row at line 97 to contain title and breadcrumb, so
<h1>{% block title %}{% endblock %}</h1>
becomes
<div class="row">
<div class="col-xs-12 col-sm-6">

<h1>{% block title %}{% endblock %}</h1>
</div>
<div class="col-sm-6 hidden-xs">
also let breadcrumb "pull-right"


Change left panel width from col-md-2 to col-md-1, delete left panel default tree
Change middle panel width from col-md-7 to {% block main_span %}col-md-10{% endblock %}
Add main_span to templates\blog\blog_post_list.html line 44
{% block main_span %}col-md-8{% endblock %}
Add main_span to templates\pages\index.html line 3
{% block main_span %}col-md-8{% endblock %}

Change right panel width from col-md-3 to {% block right_panel_span %}col-md-1{% endblock %}
Add right_panel_span to templates\blog\blog_post_list.html  line 45
{% block right_panel_span %}col-md-3{% endblock %}

Install Pagedown, a Mezzanine Markdown Package
Add "mezzanine_pagedown" to the settings.py INSTALLED_APPS list...

INSTALLED_APPS = (
    "mezzanine_pagedown",
    "django.contrib.admin",
    "django.contrib.auth",

and the following somewhere in settings.py.
#####################
# PAGEDOWN SETTINGS #
#####################
RICHTEXT_WIDGET_CLASS = 'mezzanine_pagedown.widgets.PageDownWidget'
RICHTEXT_FILTER = 'mezzanine_pagedown.filters.custom'
RICHTEXT_FILTERS = (RICHTEXT_FILTER,)
PAGEDOWN_MARKDOWN_EXTENSIONS = ('extra','codehilite','toc')
RICHTEXT_FILTER_LEVEL = 3
PAGEDOWN_SERVER_SIDE_PREVIEW = True
Server side previews are selected, so near the top of urls.py add

import mezzanine_pagedown.urls
Also in urls.py, the pagedown uri MUST go above the mezzanine "catch all" (which is near the bottom anyway). I'll put it near the top, just under "urlpatterns =".

urlpatterns = patterns("",
    ("^pagedown/", include(mezzanine_pagedown.urls)),
    
Make home page editable

Responsive Full Background Image Using CSS(http://sixrevisions.com/css/responsive-background-image/)
