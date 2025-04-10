from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, UserAccount
from .forms import DepositForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string


def email_send_user(user, amount, template, title):
    try:
        msg = render_to_string(
            template,
            {"user": user, "amount": amount, "title": title},
        )
        send_email = EmailMultiAlternatives(title, "", to=[user.email])
        send_email.attach_alternative(msg, "text/html")
        send_email.send()
    except Exception as e:
        print(e)


# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = "transaction_form.html"
    success_url = reverse_lazy("home_page")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs


class DepositMoney(TransactionCreateMixin):

    form_class = DepositForm

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        account = self.request.user.account
        if amount is None or account is None:
            messages.error(self.request, "Invalid deposit operation.")
            return self.form_invalid(form)

        try:
            account.balance += amount
            account.save(update_fields=["balance"])
            messages.success(
                self.request,
                f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully',
            )
            email_send_user(
                self.request.user,
                amount,
                "send_email.html",
                "Deposit",
            )
            return super().form_valid(form)
        except Exception as e:
            messages.error(
                self.request, "An error occurred while processing your deposit."
            )
            print(e)

            return self.form_invalid(form)


