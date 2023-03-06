from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Default django authentication
    path('', include('django.contrib.auth.urls')),

    # View page for Registration
    path('register/', views.register, name="register"),
]
