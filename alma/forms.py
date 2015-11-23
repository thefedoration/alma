from __future__ import absolute_import

from django import forms
from alma.models import Lead


class LeadForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = '__all__'