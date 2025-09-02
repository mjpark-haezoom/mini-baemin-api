# stores/consumer_views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.permissions import AllowUserTypes
from .models import Menu, Store
from .serializers import MenuSerializer, StoreListSerializer


# API view to get a list of all stores (consumer only)
class StoreListView(generics.ListAPIView):
    """
    Retrieves a list of all stores.
    """
    permission_classes = [IsAuthenticated, AllowUserTypes]
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

# API view to get the menu for a specific store (consumer only)
class MenuListView(generics.ListAPIView):
    """
    Retrieves the menu list for a specific store.
    """
    permission_classes = [IsAuthenticated, AllowUserTypes]
    serializer_class = MenuSerializer

    def get_queryset(self):
        # Filter menu items by the 'store_id' from the URL parameters
        store_id = self.kwargs["store_id"]
        return Menu.objects.filter(store_id=store_id)