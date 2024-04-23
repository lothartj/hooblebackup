from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Listing, ContactAgent
from .utils import send_email
from django.contrib import messages
from .models import Listing, Image

# Create your views here.
def homepage(request):
    listings = Listing.objects.prefetch_related('images').all()  
    images = Image.objects.all()
    return render(request, "homepage.html", {'listings': listings, 'images': images})



######################################################################################################################################
def imagecat(request):
    listings = Listing.objects.all()  # Fetch all listings from the database

    if request.method == 'POST':
        # Retrieve form data
        user_name = request.POST.get('user_name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        message = request.POST.get('message')

        # Save data into database
        contact = ContactAgent(
            user_name=user_name,
            surname=surname,
            email=email,
            mobile_number=mobile_number,
            message=message
        )
        contact.save()

        # Assuming the send_email function is defined elsewhere and configured correctly
        receiver_email = "lothartjipueja90@gmail.com"  # Update with the agent's email address
        subject = "New Contact Request"
        body = f"You have a new contact request from {user_name} {surname}. Email: {email}, Mobile Number: {mobile_number}. Message: {message}"
        # Assuming no file attachments for now
        file_paths = []
        send_email(receiver_email, subject, body, file_paths)

        # Add success message
        messages.success(request, 'Your email has been sent successfully!')
        
        # Redirect after form submission
        return redirect('imagecat')  # Redirect to the same page after form submission
    else:
        # Render the page with the listing data
        return render(request, "imagecat.html", {'listings': listings})
######################################################################################################################################