from django.contrib import admin
from .models import Ingredients


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'time', 'price', 'photo', 'quantity')
    list_display_links = ('id','name')


admin.site.register(Ingredients,IngredientsAdmin)
