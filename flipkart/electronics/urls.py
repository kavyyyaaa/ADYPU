from django.urls import path
from electronics import views
urlpatterns = [
    path('electronics/',views.home, name = "home")
]