from django.shortcuts import redirect,render,HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact


def index(request):
    return render(request,"index.html")

def Work(request):
    return render(request,"Work.html")
    
def contact(request):
    return render(request,"contact.html")
    
def contact_submit(request):
    if request.method == 'POST':
        # Get the form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create and save the contact instance
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return redirect("/")
    
    # If the request method is not POST, return an invalid request message
    return HttpResponse("Invalid request method.")

