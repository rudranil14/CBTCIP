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
