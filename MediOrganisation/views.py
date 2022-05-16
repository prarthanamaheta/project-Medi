
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, DeleteView, UpdateView

from MediOrganisation.forms import OrganisationForm

from MediOrganisation.models import organisation
from MediUser.models import MediUser


class OrganisationView(CreateView):
    model = organisation
    queryset = organisation.objects.all()
    form_class = OrganisationForm
    template_name = 'MediOrganisation/organisation.html'

    def post(self, request, *args, **kwargs):
        donor = MediUser.objects.get(username=request.user.username)
        organisation_name = request.POST['organisation_name']
        organisation_address = request.POST['organisation_address']

        s = organisation(donor_id_id=donor.id,
                         organisation_name=organisation_name,
                         organisation_address=organisation_address,
                         )
        s.save()
        return render(request, 'MediUser/base.html')


class OrganisationUpdateView(UpdateView):
    template_name = 'MediDonor/nominee.html'
    form_class = OrganisationForm
    success_url = reverse_lazy('profile')
    model = organisation


class OrganisationDeleteView(DeleteView):
    success_url = reverse_lazy('profile')
    queryset = organisation.objects.all()
