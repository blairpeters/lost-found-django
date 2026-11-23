from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from myapp.my_forms import ItemForm,RegisterForm
from django.contrib import messages
from myapp.models import Item
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404
from .models import Item
from .my_forms import ItemForm



# Create your views here.
@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


@login_required
def post_items(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
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
@login_required
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
@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item successfully updated")
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})


#delete function that avoids accidental deletion when someone visits eg http://127.0.0.1:8000/delete/5/
@login_required
@user_passes_test(lambda user: user.is_staff) #ensures Someone doesnt manually enter the deletion URL in their browser or send a POST request.
def delete_item(request, id):

    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':

        item_title = item.title
        item.delete()

        messages.success(request, f"{item_title} successfully deleted")

        return redirect('home')

    return redirect('home')
