# urls.py
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="homepage"),  # Correctly configured for the homepage
   path('imagecat/<int:listing_id>/', views.imagecat, name='imagecat'),  # Correctly configured for detailed view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
