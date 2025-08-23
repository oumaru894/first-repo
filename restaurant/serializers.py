"""this file contains serializers for the restaurant app in django"""
from rest_framework.serializers import ModelSerializer
from .models import MenuItem, Booking


class MenuItemSerializer(ModelSerializer):
    """"serializer for MenuItem model"""
    
    class Meta:
        model = MenuItem
        fields  = "__all__"

class BookingSerializer(ModelSerializer):
    """This is a serializer for booking"""
    class Meta:
        model = Booking
        fields = "__all__"
    
    
    