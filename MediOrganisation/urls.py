from django.urls import path

from MediOrganisation.views import OrganisationView, OrganisationDeleteView, OrganisationUpdateView

urlpatterns = [
    path('organisation/', OrganisationView.as_view(), name='organisation'),
    path('edit_organisation/<pk>',OrganisationUpdateView.as_view(),name='edit_organisation'),
    path('delete_organisation/<pk>', OrganisationDeleteView.as_view(), name="delete_organisation"),
]
