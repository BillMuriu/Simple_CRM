from django.urls import path
from . import views          # import views from the same directory


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customers/', views.customers, name="customers"),
]
