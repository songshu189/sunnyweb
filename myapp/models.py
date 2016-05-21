from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText

class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading welcome text")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")