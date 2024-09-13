from django.shortcuts import redirect,render,HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

# 





def index(request):
    return render(request,"index.html")

def Work(request):
    return render(request,"Work.html")
    
def contact(request):
    return render(request,"contact.html")
    




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
            message=f"Subject: {subject}\n\nMessage:\n{message}",
            from_email=email,
            recipient_list=['khodiyartravels2003@gmail.com'],  # Your email where you want to receive messages
        )

        return HttpResponse("Message sent and saved successfully!")
    else:
        return HttpResponse("Invalid request method.")




