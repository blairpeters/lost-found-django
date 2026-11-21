from django.shortcuts import render, redirect
from myproject.my_forms import ItemForm
from django.contrib import messages
from myapp.models import Item

# Create your views here.

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
