from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    # "users/profile/logout",
    # path("<str:name>/profile/", UserProfileView.as_view(), name="user_profile"),
    path("<str:name>/profile/", views.user_profile, name="user_profile"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("logout/", views.UserLogoutView.as_view(), name="user_logout"),
    path(
        "logout/confirmation/",
        views.TemplateView.as_view(template_name="logout_conf.html"),
        name="logout_conf",
    ),
    path("register/", views.UserRegisterView.as_view(), name="user_register"),
    path("return/pay/<int:id>", views.ReturnPay.as_view(), name="return_pay"),
    path(
        "<str:name>/profile/edit",
        views.EditUserProfile.as_view(),
        name="edit_user_profile",
    ),
    # path("user/account/deposit/", user_deposit, name="user_account_deposit"),
    # path("user/borrowing/history/", borrow_history, name="user_borrow_history"),
]
