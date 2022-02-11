from django.core.mail import send_mail
from django.shortcuts import render
from .models import *

# Create your views here.


def HomeView(request):
    performer = Artist.objects.order_by("list_order")
    attraction = Attraction.objects.order_by("list_order")
    aboutsection = AboutInfo.objects.all()
    return render(
        request,
        "home/home.html",
        {"performer": performer},
        {"attraction": attraction},
        {"aboutsection": aboutsection},
    )


def contact(request):
    if request.method == "POST":
        message_email = request.POST["message-email"]
        message = request.POST["message"]
        # send email
        send_mail(
            subject="NEXUS",
            message=message,
            from_email=message_email,
            recipient_list=["NexusFestivalS@gmail.com"],
        )
    return render(request, "home/home.html")


# class HomeView:
# template_name = "home/home.html"
