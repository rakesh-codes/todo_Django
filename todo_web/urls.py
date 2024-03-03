"""
URL configuration for todo_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home, name='home'),  # Define URL pattern for the homepage
    path('admin/', admin.site.urls),  # Include Django admin URLs
    path('add/', views.add, name='add'),  # Define URL pattern for adding tasks
    path('update/<int:id>/', views.update, name='update'),  # Define URL pattern for updating tasks
    path('delete/<int:id>/', views.delete, name='delete'),  # Define URL pattern for deleting tasks
    
]