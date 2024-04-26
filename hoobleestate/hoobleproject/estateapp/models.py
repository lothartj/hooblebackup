from django.db import models
from django.contrib import admin

# ContactAgent model
class ContactAgent(models.Model):
    user_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)  # Assuming mobile number won't exceed 15 characters
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.user_name} {self.surname}"

# Listing model
class Listing(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    erf_size = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    bedroom_count = models.IntegerField()
    bathroom_count = models.IntegerField()
    lounge_size = models.CharField(max_length=100)
    tv_room = models.CharField(max_length=100)
    dining_area = models.CharField(max_length=100)
    kitchen_description = models.TextField()
    entertainment_area = models.TextField()
    additional_amenities = models.TextField()
    outdoor_features = models.TextField()
    agent_email = models.EmailField()
    agent_contact_number = models.CharField(max_length=20)
    iframe_url = models.URLField()

    def __str__(self):
        return self.title

# Image model
class Image(models.Model):
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listing_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.listing.title} - {self.caption}"

# Inline admin for images
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Number of extra forms to display
    min_num = 1  # Minimum number of forms to display
    max_num = 10  # Maximum number of forms you want to allow

# Admin class for Listing
class ListingAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


