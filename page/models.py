from django.db import models
from django.urls import reverse

# Create your models here.

TYPE_CHOICES =(

    ('H','HOUSE'),
    ('A','APARTMENT'),
    ('S', 'Studion'),
    ('M', 'Mansion'),
    ('C','COttage'),
)

class Property(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=150)
    price = models.FloatField(default=0.0)
    area = models.FloatField(default=0.0, help_text="Enter area in sq. ft")
    property_type = models.CharField(choices =TYPE_CHOICES, max_length=1)
    picture = models.ImageField(upload_to='property',blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title



