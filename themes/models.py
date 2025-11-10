from django.db import models

# Create your models here.
class Feedback_us(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    service = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    