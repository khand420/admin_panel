from django.db import models

# Create your models here.


class Partner(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name