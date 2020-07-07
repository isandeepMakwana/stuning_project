from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def item_list(request):
    """
    List all code item, or create a new items.
    """
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)