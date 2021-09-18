from django.urls import path

from .views import UserDetail, RegisterView, BlackListTokenView
from rest_framework_simplejwt.views import TokenObtainPairView

#Account url pattern
urlpatterns = [
    path('profile/', UserDetail.as_view(), name="account_profile"),
    path('login/', TokenObtainPairView.as_view(), name="account_login"),
    path('register/', RegisterView.as_view(), name="account_register"),
    path('logout/', BlackListTokenView.as_view(), name="account_logout")
]
