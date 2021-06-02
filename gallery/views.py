from django.shortcuts import render, redirect
from wms.models import Atm, Order, AtmPhoto

# Create your views here.

def main(request):
    # Выводит список фотографий
    order = request.GET.get('order')
    if order == None:
        photos = AtmPhoto.objects.all()
    else:
        photos = AtmPhoto.objects.filter(order__logistic_order=order)

    orders = Order.objects.all()
    context = {'orders': orders, 'photos': photos}
    return render(request, 'gallery/main.html', context)

def view_photo(request, pk):
    photo = AtmPhoto.objects.get(id=pk)
    return render(request, 'gallery/photo.html', {'photo': photo})

def add_photo(request):
    orders = Order.objects.all()
    atms = Atm.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['order'] != 'none':
            order = Order.objects.get(id=data['order'])
        else:
            order = None
        
        if data['atm'] != 'none':
            atm = Atm.objects.get(id=data['atm'])
        else:
            atm = None

        for image in images:
            photo = AtmPhoto.objects.create(
                description=data['description'],
                order=order,
                atm=atm,
                image=image,
            )

        return redirect('gallery:main')

    context = {'orders': orders, 'atms': atms}
    return render(request, 'gallery/add.html', context)