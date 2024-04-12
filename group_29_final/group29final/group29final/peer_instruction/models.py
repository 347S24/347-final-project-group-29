from audioop import reverse
from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        """Returns the url to access a particular question instance."""
        return reverse('question-detail', args=[str(self.id)])
