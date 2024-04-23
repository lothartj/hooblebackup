from django.contrib import admin
from .models import ContactAgent, Listing, Image, ListingAdmin, ImageInline

# Register the ContactAgent model
admin.site.register(ContactAgent)

# Register the Listing model using the ListingAdmin to include the ImageInline
admin.site.register(Listing, ListingAdmin)

# Optionally, register the Image model if you want it to be manageable outside of the Listing context
# admin.site.register(Image)