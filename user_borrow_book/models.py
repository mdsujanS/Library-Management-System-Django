from django.db import models
from books.models import Book
from django.contrib.auth.models import User

# Create your models here.


class BorrowBook(models.Model):
    user = models.ForeignKey(User, related_name="borrow_user", on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name="user_borrow_book", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    borrow_at = models.DateTimeField(auto_now_add=True)
