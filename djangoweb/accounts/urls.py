from django.http import HttpResponse
from django.urls import path
from . import views

def test(request):
    return HttpResponse("Accounts URL is working!")

urlpatterns = [
    path("test/", test),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]