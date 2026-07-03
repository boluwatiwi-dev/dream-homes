"""
URL configuration for djangoweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("property/<int:id>/", views.property_detail, name="property_detail"),
    path("add-property/", views.add_property, name="add_property"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("favorite/<int:id>/", views.toggle_favorite, name="toggle_favorite"),
    path("favorites/", views.favorites, name="favorites"),
    path(
    "contact-owner/<int:id>/",
    views.contact_owner,
    name="contact_owner"
),
    path(
    "my-inquiries/",
    views.my_inquiries,
    name="my_inquiries"
),
    path("edit-property/<int:id>/", views.edit_property, name="edit_property"),
    path("delete-property/<int:id>/", views.delete_property, name="delete_property"),
]
