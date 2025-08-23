from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuItem, Booking


# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    #permission_classes = [permissions.IsAuthenticated] 
    




def index(request):

    return render("index.html")