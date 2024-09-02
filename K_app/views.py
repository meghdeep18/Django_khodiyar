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

        # send_mail(
        #     'New Contact Form Submission',  # Subject of the email
        #     f'Name: {name}\nEmail: {email}\nMessage: {message}',  # Message content
        #     settings.DEFAULT_FROM_EMAIL,  # From email (defined in settings.py)
        #     ['meghdeep219@gmail.com'],  # Recipient email(s)
        #     fail_silently=False,  # Set to True to ignore errors
        # )

        # Respond with a success message
        return redirect("/")
    
    # If the request method is not POST, return an invalid request message
    return HttpResponse("Invalid request method.")

# def blog(request):
#     return render(request,'blog.html')

# def blog_list(request):
#     posts = BlogPost.objects.all().order_by('-published_date')
#     return render(request, 'blog/blog_list.html', {'posts': posts})

# def blog_detail(request, slug):
#     post = get_object_or_404(BlogPost, slug=slug)
#     return render(request, 'blog/blog_detail.html', {'post': post})

# def category_posts(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     posts = BlogPost.objects.filter(category=category)
#     return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

