from django.shortcuts import render, redirect
from .models import Product, Tag, ColorTag
from products.forms import MyUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def index(request):
    return render(request, 'base.html')


def products_view(request):
    if "title" in request.GET:
        objects = Product.objects.filter(
            title__icontains=request.GET["title"])
    else:

        objects = Product.objects.all()
    return render(request, "products.html", {
        'objects': objects
    })


def product_like(request, product_id):
    if request.method == "POST":
        object = Product.objects.get(pk=product_id)
        if object.likes.filter(id=request.user.id).exists():
            object.likes.remove(request.user)
        else:
            object.likes.add(request.user)
    return redirect('products')


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, "product_detail.html", {
        'product': product
    })


def register_user(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, 'register.html', {
        "form": form
    })


def login_user(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")

    return render(request, "login.html", {
        "form": form
    })
def logout_user(request):
    logout(request)
    return redirect("/")