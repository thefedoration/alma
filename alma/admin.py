from __future__ import absolute_import

from alma.models import Lead

from django.contrib import admin


class LeadAdmin(admin.ModelAdmin):
    model = Lead
    list_display = ('email', 'name', 'organization', 'description', 'create_date')
    search_fields = ('email', 'name', 'organization')

admin.site.register(Lead, LeadAdmin)