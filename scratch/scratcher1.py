from django.db.models import Sum
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
import razorpay
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, TemplateView

import json

import stripe
from .models import Transaction


def payment_gateway(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        client = razorpay.Client(
            auth=("rzp_test_O9ogAcvgzwnBks", "dfJZJTm8zNS2CyEWFpiYN2BM"))
        payment = client.order.create(
            {
                'amount': amount,
                'currency': 'INR',
                'payment_capture': '1'
            }
        )
        print(payment)
        transaction_obj = Transaction(
            name=name, amount=amount, payment_id=payment['id'])
        transaction_obj.save()
        return render(request, 'MediPayment/payment.html', context={"payment": payment})

    return render(request, 'MediPayment/payment.html')


@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        order_id = data.get('razorpay_order_id', '')
        obj = Transaction.objects.filter(payment_id=order_id).first()
        try:
            obj.status = 'success'
            obj.save()
            return render(request, 'MediPayment/success.html')

        except:

            obj.status = 'fail'
            return render(request, 'MediPayment/fail.html')

    return render(request, 'MediPayment/success.html')


class PaymentStripe(View):
    def post(self, request, *args, **kwargs):


        try:

            name = request.POST.get("name")
            amount = int(request.POST.get("amount")) * 100
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='INR',
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            transaction_obj = Transaction(
                name=name, amount=amount, payment_id=intent['id'])
            transaction_obj.save()
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return jsonify(error=str(e)), 403

    if __name__ == '__main__':
        app.run(port=4242)



