from django.contrib import admin
from django.urls import path
from app import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),   # Default route
    path('home/', views.home, name='home'),    # Home page
]