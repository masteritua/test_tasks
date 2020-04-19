# accounts/urls.py
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path("profile/<int:pk>/", views.Profile.as_view(), name='profile'),
    path("profile-edit/<int:pk>/", views.ProfileEdit.as_view(), name='profile-edit'),
]
