from __future__ import absolute_import

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

import os
import sys
import sendgrid


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


"""
SIGNALS FOR CREATING LEADS
"""

@receiver(post_save, sender=Lead)
def send_lead_email(sender, instance, created, *args, **kwargs):
    if created:
        print "created!!!"
        sys.stdout.flush()
        print instance
        sys.stdout.flush()

        sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME'), os.environ.get('SENDGRID_PASSWORD'))

        message = sendgrid.Mail()
        message.add_to('Fedor Garin <fedor.garin@gmail.com>')
        message.set_subject('New Almify lead - %s' % instance.email)
        message.set_text('\n \
            Name - %s \n \
            Email - %s \n \
            Organization - %s \n \
            Description - %s \n \
            Time - %s \n \
        ' % (instance.name, instance.email, instance.organization, instance.description or "", instance.create_date))
        message.set_from('Almify Leads <leads@almify.com>')
        status, msg = sg.send(message)



