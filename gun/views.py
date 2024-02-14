from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserData
from django.utils import timezone



def send_welcome_email(name, email):
    # Customize the email content as per your requirements
    subject = "Welcome to Our Website"
    message = f"Hello, {name}, Welcome to Rapunzel Hair Affair where beauty meets elegance! In accordance to our esteemed motto we offer hair dressing, nail decoration, piercing and tatooing services. Get to book one of the sessions to enjoy the services we render.Our achievement is to have a satisfied customer."
    from_email = "bonfacemwema7@gmail.com"  # Update with your email
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]

        if UserData.objects.filter(username=name).exists():
            messages.error(request, "That username is taken")
        elif UserData.objects.filter(email=email).exists():
            messages.error(request, "That email is taken")
        else:
            if create_user_and_send_email(name, email):
                messages.success(
                    request,
                    f"A welcome email has been sent to {email}. Check your email for more information",
                )
            else:
                messages.error(
                    request, "Error creating user or sending email. Please try again."
                )

        return redirect("index")

    return render(request, "index.html")


def create_user_and_send_email(name, email):
    user = UserData(username=name, email=email)
    user.save()

    if send_welcome_email(name, email):
        return True
    else:
        # If sending email fails, you might want to handle it appropriately
        user.delete()  # Delete the user if email sending fails
        return False


def display_users(request):
    users = UserData.objects.all()
    context = {"users": users}
    return render(request, "user_list.html", context)
