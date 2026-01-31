from django.contrib import admin
from .models import Dish, Category

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'is_popular')
    list_filter = ('category', 'is_popular')

admin.site.register(Category)

