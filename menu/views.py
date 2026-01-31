from django.shortcuts import render
from .models import Dish, Category

def home(request):
    dishes = Dish.objects.all()
    categories = Category.objects.all()

    q = request.GET.get('q')
    if q:
        dishes = dishes.filter(title__icontains=q)

    category_id = request.GET.get('category')
    if category_id:
        dishes = dishes.filter(category_id=category_id)

    popular = Dish.objects.filter(is_popular=True)

    return render(request, 'menu/home.html', {
        'dishes': dishes,
        'categories': categories,
        'popular': popular
    })
