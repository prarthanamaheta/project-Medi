from django import forms

from MediOrganisation.models import organisation


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = organisation
        fields = ['organisation_name', 'organisation_address', 'organisation_mobile']
