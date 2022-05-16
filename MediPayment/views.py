import stripe
from django.core.mail import send_mail

from django.conf import settings
from django.db.models import Sum
from django.shortcuts import render, redirect

from django.views.generic import ListView, TemplateView

from MediPayment.models import Transaction

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.price_id = settings.STRIPE_PRICE_ID
YOUR_DOMAIN = settings.DOMAIN


def index(request):
    return render(request, 'MediPayment/payment.html')


def create_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': stripe.price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/payment/success/',
            cancel_url='http://127.0.0.1:8000/payment/fail/',
        )
        request.session['payment_id'] = checkout_session.id

    except stripe.error.CardError as e:
        print("A payment error occurred: {}".format(e.user_message))

    return redirect(checkout_session.url, code=303)


class FailView(TemplateView):
    template_name = 'MediPayment/fail.html'


class SuccessView(TemplateView):
    template_name = 'MediPayment/success.html'

    def get(self, request, *args, **kwargs):
        session = stripe.checkout.Session.retrieve(
            request.session['payment_id'],
            expand=['customer_details']
        )
        try:
            if session.status == 'complete':
                t = Transaction(payment_id=request.session['payment_id'],
                                amount=session.amount_total / 100, status='success',
                                name=session.customer_details.name,
                                email=session.customer_details.email)
                t.save()
                subject = 'Thanking for donation'
                message = f'Hi {session.customer_details.name}, thank you for donating and helping MediCare.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [session.customer_details.email, ]
                send_mail(subject, message, email_from, recipient_list)
                return render(request, 'MediPayment/success.html')

        except:

            t = Transaction(payment_id=request.session['payment_id'],
                            amount=session.amount_total, status='fail',
                            name=session.customer_details.name)
            t.save()
            return render(request, 'MediPayment/fail.html')


class AmountSum(ListView):
    queryset = Transaction.objects.filter(status='success')
    template_name = 'MediUser/home.html'
    context_object_name = 'pro'

    def get_queryset(self):
        return self.queryset.aggregate(amount=Sum('amount'))
