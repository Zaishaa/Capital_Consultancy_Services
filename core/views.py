from django.shortcuts import render
from .models import Lead

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        role = request.POST.get("role")

        Lead.objects.create(
            name=name,
            email=email,
            phone=phone,
            role=role
        )

    return render(request, "home.html")
