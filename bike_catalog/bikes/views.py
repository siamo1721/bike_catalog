
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bike
from .forms import BikeForm


def bike_detail(request, id):
    bike = get_object_or_404(Bike, id=id)
    return render(request, 'bikes/bike_detail.html', {'bike': bike})

def edit_bike(request, id):
    bike = get_object_or_404(Bike, id=id)

    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return redirect('bikes:bike_list')
    else:
        form = BikeForm(instance=bike)

    return render(request, 'bikes/edit_bike.html', {'form': form, 'bike': bike})

def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes/bike_list.html', {'bikes': bikes})

def add_bike(request):
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Bike saved successfully")
            return redirect('bikes:bike_list')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = BikeForm()
    return render(request, 'bikes/bike_form.html', {'form': form})

def delete_bike(request, id):
    bike = get_object_or_404(Bike, id=id)
    bike.delete()
    return redirect('bikes:bike_list')
