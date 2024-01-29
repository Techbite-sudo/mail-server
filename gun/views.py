from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def send_welcome_email(name, email):
    # Customize the email content as per your requirements
    subject = "Welcome to Our Website"
    message = (
        f"Hello, {name}, Welcome to Rapunzel Hair Affair where beauty meets elegance! In accordance to our esteemed motto we offer hair dressing, nail decoration, piercing and tatooing services. Get to book one of the sessions to enjoy the services we render.Our achievement is to have a satisfied customer."
    )
    from_email = "bonfacemwema7@gmail.com"  # Update with your email
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return True
    except Exception as e:
        return False


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]

        if send_welcome_email(name, email):
            messages.success(request, "A welcome email has successfully been sent to "+email+". Check your email for more information")
        else:
            messages.error(request, "Error sending email. Please try again.")

    return render(request, "index.html")
