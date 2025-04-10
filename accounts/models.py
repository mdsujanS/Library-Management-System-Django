from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    account_create_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    account = models.ForeignKey(
        UserAccount, related_name="transaction", on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        ordering = ["timestamp"]
