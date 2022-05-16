from django.urls import path

from MediPayment.views import AmountSum
from MediUser import views

from MediUser.views import RegisterPage, LogingView, LogingOutView, PasswordUpdateView, UserUpdateView

urlpatterns = [
    path('', AmountSum.as_view(), name='home'),
    path('base/', views.DonorPage, name='base'),
    path('profile/', views.profile_page, name='profile'),
    path('signup/', RegisterPage.as_view(), name='signup'),
    path('login/', LogingView.as_view(), name='login'),
    path('logout/', LogingOutView.as_view(), name='logout'),
    path('edit_password/<pk>', PasswordUpdateView.as_view(), name="edit_password"),
    path('edit_user/<pk>', UserUpdateView.as_view(), name="edit_user"),
]
