from django.db import models

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    image = models.ImageField(upload_to='Api_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description
