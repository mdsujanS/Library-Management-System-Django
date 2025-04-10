from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import Book, AddReview
from .forms import AddBookForm, AddReviewForm
from user_borrow_book.models import BorrowBook
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import HttpResponse


class BookDetail(DetailView):
    model = Book
    template_name = "book_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "book"
    form_class = AddReviewForm

    def get(self, request, *args, **kwargs):
        user = request.user
        self.object = self.get_object()
        book_id = self.object.id
        book_title = self.object.title
        if self.request.user.is_authenticated:
            borrow_books = BorrowBook.objects.filter(user=user, book_id=book_id)
            if borrow_books:
                form = self.form_class()
                context = self.get_context_data(object=self.object, form=form)
                return self.render_to_response(context)

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        book_id = self.object.id
        book_title = self.object.title
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = self.object
            review.save()
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        book_title = book.title
        book = Book.objects.get(title=book_title)
        review_all = book.reviews.all()
        context["review_all"] = review_all
        return context


class ShowAllBook(ListView):
    model = Book
    template_name = "all_books.html"

    context_object_name = "all_books"


class AddBook(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = "add_book.html"
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        form.save()
        messages.success(request, "Successfully added this book.....")
        return super().form_valid(form)
