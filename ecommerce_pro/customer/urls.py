from django.urls import path
from . import views

urlpatterns = [
    path('customer_manage/', views.customer_details_manage, name="customer_manage")
]