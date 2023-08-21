from django.shortcuts import render, redirect
from . forms import ProductForm
from . models import Product
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def showProduct(request):
    products = Product.objects.filter().order_by('-created_at')
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page':page}
    return render(request, 'show-product.html', context)

def createProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ShowProduct')
    context = {'form':form}
    return render(request, 'create-product.html', context)

def viewProduct(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product':product}
    return render(request, 'view-product.html', context)

def updateProduct(request, slug):
    product = Product.objects.get(slug=slug)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ShowProduct')
    context = {'product':product, 'form':form}
    return render(request, 'update-product.html', context)

def deleteProduct(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == "POST":
        product.delete()
        return redirect('ShowProduct')
    context = {'product':product}
    return render(request, 'delete-product.html', context)

def search(request):
    products = Product.objects.all()
    if request.method == "GET":
        query = request.GET.get('query')
        query_set = products.filter(Q(name__icontains=query) | Q(price__icontains=query))
        
        paginator = Paginator(query_set, 3)
        page = request.GET.get('page')
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
            
    return render(request, 'layout/search.html', { 'query':query, 'page':page})
    