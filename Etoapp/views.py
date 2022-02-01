from django.shortcuts import render, redirect
from .models import Order , Cars
from .form import CarForm , OrderForm


# Create your views here.
def index(request):
    template = 'Etoapp/index.html'
    context = {}
    car = Cars.objects.all()[:3]
    context['cars'] = car
    return render(request, template, context)


def car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = CarForm
    return render(request, 'Etoapp/add.html', {'form': form})

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm()
    return render(request, 'Etoapp/index.html', {'formfromkairat': form})