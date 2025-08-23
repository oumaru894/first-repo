from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Initialize APIClient
        self.client = APIClient()
        
        # Create test instances of the Menu model
        self.menu1 = MenuItem.objects.create(name="Pizza", price=10.99)
        self.menu2 = MenuItem.objects.create(name="Burger", price=8.99)
        self.menu3 = MenuItem.objects.create(name="Pasta", price=12.50)

    def test_getall(self):
        # Send GET request to the endpoint that lists all Menu items
        response = self.client.get('/api/menu/')
        
        # Serialize all Menu objects
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        
        # Assert that the response data equals the serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
