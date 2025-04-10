from django.contrib import admin
from .models import BorrowBook


# Register your models here.
@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ["user", "book", "quantity", "borrow_at"]
