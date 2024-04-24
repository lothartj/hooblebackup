from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Listing, ContactAgent
from .utils import send_email
from django.contrib import messages
from .models import Listing, Image, ListingAdmin
from django.shortcuts import render, get_object_or_404

# Create your views here.
def homepage(request):
    listings = Listing.objects.prefetch_related('images').all()
    return render(request, 'homepage.html', {'listings': listings})



######################################################################################################################################
def imagecat(request, listing_id=None):
    # Fetch the specific listing based on the listing_id if provided
    if listing_id:
        listing = get_object_or_404(Listing.objects.prefetch_related('images'), id=listing_id)
    else:
        listing = None

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

        # Email sending logic (assuming the send_email function is defined elsewhere and configured correctly)
        receiver_email = {Listing.agent_email}  # Update with the agent's email address
        subject = "Property Listing Inquire"
        body = f"{user_name} {surname} would like to Inquire about your recent listing {listing.title}. Email: {email}, Mobile Number: {mobile_number}. Message: {message}"
        # Assuming no file attachments for now
        file_paths = []
        send_email(receiver_email, subject, body, file_paths)

        # Add success message
        messages.success(request, 'Your email has been sent successfully!')
        
        # Redirect after form submission
        if listing_id:
            return redirect('imagecat', listing_id=listing_id)
        else:
            return redirect('imagecat')
    else:
        # Render the page with the listing and its images
        return render(request, "imagecat.html", {'listing': listing, 'images': listing.images.all() if listing else []})
######################################################################################################################################