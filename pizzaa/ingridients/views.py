from django.shortcuts import render
from django.http import HttpResponse
from .models import IngredientsTypes, Ingredients
from django.http import JsonResponse
from .models import Ingredients

#date = {
 #   'title': 'Գլխաոր էջ',
#    'values': {
#        'Խմոր': ['Մեծ Խմոր', "Փոքր խմոր"],
 #       'Համեմունք': ['Զեյթուն', 'Սունկ', 'Լոլիկ'],
  #      'Սոուս': ['Մայոնեզ', 'Կծու սոուզ', 'Քաղցր սոուզ'],
   #     'Մսամթերք': ['Երշիկ', 'Բաստուրմա', 'Հավի միս', 'Տավարի միս'],
    #    'Պանիր': ['Հալած պանիր', 'Չանախ', 'Սուլուգունի']
    #}
#}


def index(request):
    data = {
        'ingredients': list(Ingredients.objects.values('name', 'type'))

    }
    return JsonResponse(data)
   # return render(request, 'ingridients/index.html', date)



def process_order(request):
    if request.method == 'POST':
        selected_spices = request.POST.getlist('selected_spices')

    return render(request, 'ingredients/order_confirmation.html', {'selected_spices': selected_spices})


