from django.urls import path
from .views import DepositMoney

urlpatterns = [
    # path("account/details/<int:id>", account_details, name="user_account_detail"),
    # path(
    #     "account/transactions/report/<int:id>",
    #     user_account_transaction_report,
    #     name="user_account_transactions_report",
    # ),
    path("deposit/", DepositMoney.as_view(), name="deposit_money"),
]
