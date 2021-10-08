from django.shortcuts import render, HttpResponse
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import NUMERIC_TYPES, Distance
from django.views.generic.base import TemplateView
from .models import Shop, Bank, Restaurant, Hotel, Somewhere
from django.contrib.postgres.search import SearchVector



latitude = 34.01979
longitude = -6.82829




user_location = Point(longitude, latitude, srid=4326)


def searchplaces(request):
    if request.method =="POST":
        searched = request.POST['searched']
        places = Somewhere.objects.annotate(search=SearchVector('name'),distance=Distance("location",user_location)).filter(search=searched).order_by("distance")[0:6]
        return render(request, 'shops/search.html',{'searched':searched,'places':places})
    else:
        return render(request, 'shops/search.html',{})

class Home(TemplateView):
    template_name = "shops/index.html"
    

class Banks(generic.ListView):
    model = Bank
    context_object_name = 'banks'
    queryset = Bank.objects.annotate(distance=Distance("location",user_location)).order_by("distance")[0:6]
    template_name = "shops/nearbybks.html"
    

class Shops(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance("location",user_location)).order_by("distance")[0:6]
    template_name = "shops/nearbysp.html"

class Restaurants(generic.ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    queryset = Restaurant.objects.annotate(distance=Distance("location",user_location)).order_by("distance")[0:6]
    template_name = "shops/nearbyrt.html"

class Hotels(generic.ListView):
    model = Hotel
    context_object_name = 'hotels'
    queryset = Hotel.objects.annotate(distance=Distance("location",user_location)).order_by("distance")[0:6]
    template_name = "shops/nearbyhl.html"
