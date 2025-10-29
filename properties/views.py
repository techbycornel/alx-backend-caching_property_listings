from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    data = list(properties.values())
    properties = Property.objects.all().values(
        "id", "title", "price", "location", "description"
    )
    return JsonResponse({
        "status": "success",
        "count": properties.count(),
        "data": list(properties)
    })

class PropertyListView(View):
    def get(self, request):
        properties = Property.objects.all().values("id", "title", "price", "location", "description")
        return JsonResponse(list(properties), safe=False)
