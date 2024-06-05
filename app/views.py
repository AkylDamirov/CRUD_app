from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Product
from .forms import UserForm, ProductForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users':users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user':user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form':form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)

    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form':form})


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'user_confirm_delete.html', {'user':user})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products':products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product':product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'product_form.html', {'form':form})



def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form':form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product':product})















