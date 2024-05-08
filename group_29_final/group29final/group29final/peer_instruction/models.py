import os
from django.urls import reverse
from io import BytesIO
from django.db import models
import qrcode
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.conf import settings

# Create your models here.


def generate_image_filename(instance, filename):
    # Generate a unique filename for the image based on the question ID
    return f"question_images/{instance.id}/{filename}"
    

class Question(models.Model):
    text = models.CharField(max_length=200)
    qr_code_img = models.ImageField(null=True, blank=True, upload_to="qr_codes")
    image = models.ImageField(upload_to=generate_image_filename, blank=True, null=True)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        """Returns the url to access a particular question instance."""
        url = reverse('student_answer', args=[self.id])
        domain = "http://142.93.64.74:8000"
        full_url = f"{domain}{url}"  # Add the domain and protocol
        print("Generated URL:", full_url)  # Print the generated URL for debugging
        return full_url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.get_absolute_url())  # Use the URL of the question detail page as data for the QR code
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        # Save the QR code image to filesystem
        filename = f"qr_codes/{self.id}.png"
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        img.save(filepath)
        # Set the QR code image field of the question instance
        self.qr_code_img.name = filename
        super().save(*args, **kwargs)


class Answer(models.Model):
    name = models.CharField(max_length=150, blank=True)  # Add this line
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
