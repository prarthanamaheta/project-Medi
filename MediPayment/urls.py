from django.urls import path
from . import views
from .views import AmountSum, SuccessView, FailView

urlpatterns = [
    path('amount/',AmountSum.as_view(),name='amount'),
    path('',views.create_checkout_session,name='payment'),
    path('success/',SuccessView.as_view(),name='success'),
    path('fail/',FailView.as_view(),name='fail'),
]
