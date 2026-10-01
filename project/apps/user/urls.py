from django.urls import path
from .views import SignUp, Login, Logout, Profile

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('profile', Profile.as_view(), name='profile'),
]