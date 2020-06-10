from django.urls import path

from . import views

# class based view using
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]