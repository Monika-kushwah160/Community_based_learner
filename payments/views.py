import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from sessions_app.models import Session
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request, session_id):

    session = get_object_or_404(Session, id=session_id)

    checkout_session = stripe.checkout.Session.create(

        payment_method_types=["card"],

        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": session.title,
                },
                "unit_amount": 1000,
            },
            "quantity": 1,
        }],

        mode="payment",

        success_url="http://127.0.0.1:8000/payments/success/",
        cancel_url="http://127.0.0.1:8000/payments/cancel/",

    )

    return redirect(checkout_session.url)

def payment_success(request):

    return render(request, "payments/success.html")