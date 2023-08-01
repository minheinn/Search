from django.shortcuts import render, redirect
from . forms import ProductForm
from . models import Product
from django.db.models import Q

# Create your views here.
def showProduct(request):
    products = Product.objects.all()
    context = {'products':products}
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

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ShowProduct')
    context = {'product':product, 'form':form}
    return render(request, 'update-product.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('ShowProduct')
    context = {'product':product}
    return render(request, 'delete-product.html', context)

def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))
            return render(request, 'layout/search.html', {'products':products, 'query':query})
        else:
            print("No information to show!")
            return render(request, 'layout/search.html', {})