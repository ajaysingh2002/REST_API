from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ajay_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image', views.image_gallary, name='image_gallery'), # Make sure this matches exactly
    path('api/', include('ajay_app.urls')),  # Include API URLs
    path('',views.home,name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
