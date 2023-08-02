from django.urls import path
from . import views

urlpatterns = [
    path('', views.showProduct, name="ShowProduct"),
    path('create-product/', views.createProduct, name="AddProduct"),
    path('update-product/<slug>/', views.updateProduct, name="UpdateProduct"),
    path('delete-product/<slug>/', views.deleteProduct, name="DeleteProduct"),

    path('search/', views.search, name = "search"),
]