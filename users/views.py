from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (
    TemplateView,
    UpdateView,
    FormView,
    ListView,
)
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from accounts.models import UserAccount
from user_borrow_book.models import BorrowBook
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from accounts.views import email_send_user


# Create your views here.
class UserRegisterView(FormView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("user_register")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        UserAccount.objects.create(user=user)
        messages.success(self.request, "You Are Successfully Registered!!")
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = UserLoginForm

    # def form_valid(self, form):
    #     messages.success(self.request, "You Are Successfully Login!!")
    #     return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "You Are Please Provided right information for  Login!!"
        )
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "You Are Successfully Login!!")
        return reverse_lazy("home_page")


class UserLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "You have been successfully logged out!")
        return reverse_lazy("home_page")


@login_required(login_url="user_login")
def user_profile(request, name):

    user = request.user
    user_accounts = UserAccount.objects.filter(user=user)

    borrow_books = BorrowBook.objects.filter(user=user)

    return render(
        request,
        "user_profile.html",
        {"all_borrow": borrow_books, "user_account": user_accounts},
    )


class ReturnPay(LoginRequiredMixin, View):

    def get(self, request, id):
        user_borrow = get_object_or_404(BorrowBook, id=id)
        if user_borrow:
            user_account = user_borrow.user.account
            user_borrow_book = user_borrow.book
            user_account.balance += user_borrow_book.price
            user_account.save(update_fields=["balance"])
            user_borrow.delete()
            user_borrow_book.stk_quantity += 1
            user_borrow_book.save(update_fields=["stk_quantity"])
            print(user_borrow.total_price)
            email_send_user(
                self.request.user,
                user_account.balance,
                "send_email.html",
                "Return",
            )
            messages.success(request, "You have been successfully return ")

        return redirect("user_profile", self.request.user.username)


class EditUserProfile(LoginRequiredMixin, TemplateView):
    template_name = "edit_user_profile.html"
