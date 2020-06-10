from django.urls import path
from . import views
# function based view
urlpatterns = [
    path('',views.listele,name="bloglistele"),
    
]
