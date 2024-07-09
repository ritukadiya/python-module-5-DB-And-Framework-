"""
URL configuration for pharmacy_management project.

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
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/add_product/', views.admin_add_product, name='admin_add_product'),
    path('admin/add_product_subcategory/', views.admin_add_product_subcategory, name='admin_add_product_subcategory'),
    path('admin/view_products/', views.admin_view_products, name='admin_view_products'),
    path('admin/edit_product/<int:pk>/', views.admin_edit_product, name='admin_edit_product'),
    path('admin/edit_product_subcategory/<int:pk>/', views.admin_edit_product_subcategory, name='admin_edit_product_subcategory'),
    path('admin/delete_product/<int:pk>/', views.admin_delete_product, name='admin_delete_product'),
    path('admin/delete_product_subcategory/<int:pk>/', views.admin_delete_product_subcategory, name='admin_delete_product_subcategory'),
    path('product_manager/search/', views.product_manager_search, name='product_manager_search'),
]

