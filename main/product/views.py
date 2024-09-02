from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request,'product/index.html')

def item(request):
    return render(request,'product/items.html')