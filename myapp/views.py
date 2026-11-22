from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from myapp.my_forms import ItemForm,RegisterForm
from django.contrib import messages
from myapp.models import Item
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Item
from .my_forms import ItemForm



# Create your views here.
#@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
def post_items(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
    #     validate user input
        if form.is_valid():
            form.save()
            messages.success(request, "Item successfully posted")
            return redirect('home')
    else:
        form = ItemForm()

    return render(request, 'post_items.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        #built in authentication form
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')
def register(request):
    if request.method == 'POST':
        #built in django authentication form
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= RegisterForm()
    return render(request, 'registration/signup.html',{'form':form})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

