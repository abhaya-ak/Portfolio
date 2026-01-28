# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import QueryForm
from .models import Profile, Project, Service  # if you need them

def landing(request):
    return render(request, 'landing.html')

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    services = Service.objects.all()
    return render(request, 'home.html', {'profile': profile, 'projects': projects, 'services': services})

def query_view(request):
    # debugging prints — remove when everything works
    print("query_view called, method:", request.method)

    if request.method == "POST":
        form = QueryForm(request.POST)
        print("Form bound:", form.is_bound)
        if form.is_valid():
            print("Form valid — sending mail")
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            print("1")
            full_message = (
                f"Name: {name}\n"
                f"Email: {email}\n\n"
                f"Message:\n{message}"
            )
            print("2")
            send_mail(
                subject=f"[Query] {subject}",
                message=full_message,
                from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "webmaster@localhost"),
                recipient_list=["abhayakunwar502@gmail.com"],  # FIXED email
                fail_silently=False,
            )

            print("Mail sent successfully")
            return redirect("home")  # or show a success page
        else:
            print("Form errors:", form.errors)
    else:
        form = QueryForm()

    # If you want the contact form on home.html, include the same contexts as `home`
    profile = Profile.objects.first()
    projects = Project.objects.all()
    services = Service.objects.all()

    return render(request, "home.html", {
        "form": form,
        "profile": profile,
        "projects": projects,
        "services": services,
    })