from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="contacts",
    null=True,
    blank=True
)

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class EmergencyContact(models.Model):

    SERVICE_CHOICES = [

        ("Police", "Police"),
        ("Ambulance", "Ambulance"),
        ("Fire Brigade", "Fire Brigade"),
        ("Women Helpline", "Women Helpline"),
        ("Child Helpline", "Child Helpline"),
        ("Blood Bank", "Blood Bank"),
        ("Hospital", "Hospital"),
        ("Mental Health", "Mental Health"),

    ]

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    country = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    description = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):

        return f"{self.service} - {self.city}"