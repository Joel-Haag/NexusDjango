from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import DateRel


def contact(request):
    print("1")
    if request.method == "POST":
        message_email = request.POST["message-email"]
        message = request.POST["message"]
        print("2")
        # lol
        # send email
        send_mail(
            subject="NEXUS",
            message=message,
            from_email=message_email,
            recipient_list=["NexusFestivalS@gmail.com"],
        )
    return render(request, "home/home.html")


class HomeView(generic.ListView):
    template_name = "home/home.html"
    context_object_name = "date_info"

    def get_queryset(self):
        """Return Date."""
        return DateRel.objects.order_by("-pub_date")[:5]
