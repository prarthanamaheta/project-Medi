from django.urls import path

from MediDonor.views import PostView, NomineeView, DonateView, PostingView, PostDeleteView, NomineeDeleteView, \
    DonateDeleteView, NomineeUpdateView, PostUpdateView, DonateUpdateView, DonationView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('posting/', PostingView.as_view(), name='posting'),
    path('nominee/', NomineeView.as_view(), name='nominee'),
    path('donate/', DonateView.as_view(), name='donate'),
    path('available-donation',DonationView.as_view(),name="available_donation"),
    path('edit_nominee/<pk>', NomineeUpdateView.as_view(), name="edit_nominee"),
    path('edit_post/<pk>', PostUpdateView.as_view(), name="edit_post"),
    path('edit_donation/<pk>', DonateUpdateView.as_view(), name="edit_donation"),
    path('delete_post/<pk>', PostDeleteView.as_view(), name="delete_post"),
    path('delete_nominee/<pk>', NomineeDeleteView.as_view(), name="delete_nominee"),
    path('delete_donation/<pk>', DonateDeleteView.as_view(), name="delete_donation"),
]
