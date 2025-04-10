from django.contrib import admin
from .models import Book, AddReview

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "stk_quantity", "borrow_price", "is_available")


@admin.register(AddReview)
class Review(admin.ModelAdmin):
    list_display = ("user", "body", "created_on")
