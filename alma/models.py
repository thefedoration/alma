from __future__ import absolute_import

from django.db import models


class Lead(models.Model):

    """
    Record of someone entering their name and email on the landing page
    """
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True, blank=False, null=False)
    organization = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.email)