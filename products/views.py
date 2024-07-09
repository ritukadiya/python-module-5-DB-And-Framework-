from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductSubCategory
from .forms import ProductForm, ProductSubCategoryForm

def admin_add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_view_products')
    else:
        form = ProductForm()
    return render(request, 'products/admin_add_product.html', {'form': form})

def admin_add_product_subcategory(request):
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_view_products')
    else:
        form = ProductSubCategoryForm()
    return render(request, 'products/admin_add_product_subcategory.html', {'form': form})

def admin_view_products(request):
    products = Product.objects.all()
    subcategories = ProductSubCategory.objects.all()
    return render(request, 'products/admin_view_products.html', {'products': products, 'subcategories': subcategories})

def admin_edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_view_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/admin_edit_product.html', {'form': form})

def admin_edit_product_subcategory(request, pk):
    subcategory = get_object_or_404(ProductSubCategory, pk=pk)
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('admin_view_products')
    else:
        form = ProductSubCategoryForm(instance=subcategory)
    return render(request, 'products/admin_edit_product_subcategory.html', {'form': form})

def admin_delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('admin_view_products')

def admin_delete_product_subcategory(request, pk):
    subcategory = get_object_or_404(ProductSubCategory, pk=pk)
    subcategory.delete()
    return redirect('admin_view_products')

def product_manager_search(request):
    query = request.GET.get('q')
    subcategories = ProductSubCategory.objects.filter(product__name__icontains=query)
    return render(request, 'products/product_manager_search.html', {'subcategories': subcategories})
