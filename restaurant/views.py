from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def index(request):
    menu_item_1 = MenuItem()
    menu_item_1.name = 'Salad'
    menu_item_1.description = 'A healthier choice'
    menu_item_1.img = 'img/gallery/01.jpg'
    menu_item_1.price = 45

    menu_item_2 = MenuItem()
    menu_item_2.name = 'Peperoni Pizza'
    menu_item_2.description = 'Taste from Italy'
    menu_item_2.img = 'img/gallery/02.jpg'
    menu_item_2.price = 70

    menu_item_3 = MenuItem()
    menu_item_3.name = 'Bread'
    menu_item_3.description = 'A piece of the meditteranian'
    menu_item_3.img = 'img/gallery/03.jpg'
    menu_item_3.price = 30

    menu_items = [menu_item_1, menu_item_2, menu_item_3]
    return render(request, 'index.html', {'menu_items': menu_items})
