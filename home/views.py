from django.core.mail import send_mail
from django.shortcuts import render
from .models import *

# Create your views here.


def HomeView(request):
    navbar = NavbarHeading.objects.all().first()
    performer = Artist.objects.order_by("list_order")
    attraction = Attraction.objects.order_by("list_order")
    about_section = AboutInfo.objects.all().first()
    front_image = FrontImage.objects.all()
    front_heading = FrontHeading.objects.all().first()

    # sponsor name and their images
    sponsors = Sponsor.objects.all()

    return render(
        request,
        "home/home.html",
        {
            "navbar": navbar,
            "performer": performer,
            "attraction": attraction,
            "about_section": about_section,
            "sponsors": sponsors,
            "front_image": front_image,
            "front_heading": front_heading,
        },
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
