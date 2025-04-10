from django.db import models
from authors.models import Author
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    book_image = models.ImageField(upload_to="media/book_images")
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(to=Category)
    book_content = models.TextField()
    description = models.TextField()
    isbn_number = models.CharField(max_length=13, unique=True)
    borrow_price = models.PositiveIntegerField()
    stk_quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=50)

    @property
    def price(self):
        return self.borrow_price - self.discount_price

    def __str__(self):
        return self.title


class AddReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
