from django.urls import path
from . import views

urlpatterns = [
    path('', views.showProduct, name="ShowProduct"),
    path('create-product/', views.createProduct, name="AddProduct"),
    path('update-product/<str:pk>/', views.updateProduct, name="UpdateProduct"),
    path('delete-product/<str:pk>/', views.deleteProduct, name="DeleteProduct"),

    path('search/', views.search, name = "search"),
]