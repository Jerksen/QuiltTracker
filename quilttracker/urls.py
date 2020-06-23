from django.urls import path
from . import views

appname = "quilttracker"
urlpatterns = [
    path("", views.customer_list, name="customers"),
    path("customer/<int:pk>", views.customer_detail, name="customer_detail"),
    path("customer/new/", views.customer_new, name="customer_new"),
    path("customer/<int:pk>/edit/", views.customer_edit, name="customer_edit"),
]
