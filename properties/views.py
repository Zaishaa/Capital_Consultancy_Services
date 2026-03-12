from django.shortcuts import render
from .models import Property

def property_search(request):

    query = request.GET.get('q')

    if query:
        properties = Property.objects.filter(location__icontains=query)
    else:
        properties = Property.objects.all()

    context = {
        'properties': properties
    }

    return render(request, 'property/property_list.html', context)
# Create your views here.
