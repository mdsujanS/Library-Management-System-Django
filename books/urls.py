from django.urls import path
from .views import BookDetail, ShowAllBook, AddBook

urlpatterns = [
    path("<str:book_title>/<int:id>/", BookDetail.as_view(), name="book_detail"),
    path("show/all/", ShowAllBook.as_view(), name="show_all_books"),
    path("book/add/", AddBook.as_view(), name="add_book"),
    # path("categories/", BookCategories, name="books_category"),
    # path("popular/", books_popular_views, name="popular_books"),
]
