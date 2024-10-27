from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'description', 'release_date', 'title']  # Removed leading space
