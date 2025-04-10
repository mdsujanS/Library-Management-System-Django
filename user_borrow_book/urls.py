from django.urls import path
from . import views

urlpatterns = [
    path("book/<str:book_title>/<int:book_id>/", views.borrow_now, name="borrow_now"),
    path(
        "borrow/confirmation/<int:book_id>/",
        views.borrow_confirmation,
        name="borrow_conf",
    ),
]
