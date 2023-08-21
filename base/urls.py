from django.urls import path
from . import views

urlpatterns = [
    path('', views.showProduct, name="ShowProduct"),
    path('create-product/', views.createProduct, name="AddProduct"),
    path('update-product/<str:slug>/', views.updateProduct, name="UpdateProduct"),
    path('delete-product/<slug>/', views.deleteProduct, name="DeleteProduct"),
    path('detail-product/<slug>/', views.viewProduct, name="ViewProduct"),

    path('search/', views.search, name = "search"),
]