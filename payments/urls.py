from django.urls import path
from . import views

urlpatterns = [

    path("checkout/<int:session_id>/", views.checkout, name="checkout"),

    path("success/", views.payment_success, name="payment_success"),

]