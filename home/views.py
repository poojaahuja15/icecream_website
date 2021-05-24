from django.shortcuts import render, redirect
from home.models import Contact, Flavors
import pyautogui as pu

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def flavors(request):
    if request.method=="POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        email = request.POST.get('email')
        flavour = request.POST.get('flavour')

        d = Flavors(name=name, address=address, phone=phone, city=city, email=email, flavour=flavour)
        d.save()
        pu.confirm("Order is confirmed !!")
        return redirect('/')

    else:
        return render(request, 'flavors.html')

def dessert(request):
    return render(request, 'dessert.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method=="POST":
        f_name = request.POST.get('f_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        c = Contact(f_name=f_name, email=email, phone=phone, message=message)
        c.save()
        return render(request, 'index.html')

    else:
        return render(request, 'contact.html')