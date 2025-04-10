from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from categories.models import Category
from books.models import Book
from accounts.models import UserAccount


def HomePage(request, category_slug=None):
    books = Book.objects.all()[:12]

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = Book.objects.filter(categories=category)
    categories = Category.objects.all()
    # Compute prices for each book

    return render(
        request,
        "index.html",
        {
            "books": books,
            "categories": categories,
        },
    )
