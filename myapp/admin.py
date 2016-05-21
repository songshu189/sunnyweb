from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import HomePage

admin.site.register(HomePage, PageAdmin)