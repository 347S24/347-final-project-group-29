from audioop import reverse
from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=200)
    qr_code_img = models.ImageField(null=True, blank=True, upload_to="qr_codes")

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        """Returns the url to access a particular question instance."""
        return reverse('question-detail', args=[str(self.id)])


class Answer(models.Model):
    name = models.CharField(max_length=150, blank=True)  # Add this line
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
