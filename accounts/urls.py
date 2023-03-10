from django.urls import path
from . import views          # import views from the same directory


urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),

    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customers/<str:pk_test>/', views.customers, name="customers"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
