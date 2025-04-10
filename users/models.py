from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ReaderUserAddress(models.Model):
    user = models.OneToOneField(User, related_name="address", on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.email)
