from django.urls import path
from .views import NewHomePage


urlpatterns = [
    path("", NewHomePage.as_view(), name="home-page")
]