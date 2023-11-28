from django.urls import path
from .views import NewHomePage, PropertyDetailPage


urlpatterns = [
    path("", NewHomePage.as_view(), name="home-page"),
    path("<str:id>/", PropertyDetailPage.as_view(), name="detail-page")
]

