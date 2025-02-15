
from django.urls import path
from .views import UserRegistrationView, UserLoginView,UserBankAccountUpdateView, UserPasswordChangeView

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('profile/password_change/', UserPasswordChangeView.as_view(), name='password_change'),
]