from django.shortcuts import redirect,render,HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request,"index.html")

def Work(request):
    return render(request,"Work.html")
    
def contact(request):
    return render(request,"contact.html")
    
def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")



def signup_func(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cnfpassword = request.POST.get('cnfpassword')

        
        
        master = Master(name=name, email=email, password=password, cnfpassword=cnfpassword)
        master.save()

        return redirect('/')
    
    return render(request, 'login.html')


def login_func(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        password = request.POST.get('password')
        master = Master.authenticate(name=name, password=password)

    if user is not None:
        login(request, user)


def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the data to the Contact model
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Send the email
        send_mail(
            subject=f"Contact Form Submission from {name}",
            # message=f"Email: {email}\n\n{message}",
            message=f"Subject: {subject}\n\nMessage:\n{message}",
            from_email=email,
            recipient_list=['khodiyartravels2003@gmail.com'],  # Your email where you want to receive messages
        )

        return HttpResponse("Message sent and saved successfully!")
    else:
        return HttpResponse("Invalid request method.")
