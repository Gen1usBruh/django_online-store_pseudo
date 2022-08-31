from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_catalog, name='products-catalog'),
    path('<int:category_id>/', views.products_catalog, name='product-category'),
    path('page/<int:page>/', views.products_catalog, name='page'),
    path('basket_add/<int:product_id>/', views.basket_add, name='basket-add'),
    path('basket_delete/<int:basket_id>/', views.basket_delete, name='basket-delete'),
    
]
