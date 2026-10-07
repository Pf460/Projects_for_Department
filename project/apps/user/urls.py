from django.urls import path
from .views import SignUp, Login, Logout, Profile
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('profile', Profile.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #обновление refresh-токена
]