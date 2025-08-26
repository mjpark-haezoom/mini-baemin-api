# stores/views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.permissions import IsUserType
from .models import Store, Menu
from .serializers import StoreListSerializer, MenuSerializer, StoreCreateSerializer


# API view to get a list of all stores (public)
class StoreListView(generics.ListAPIView):
    """
    Retrieves a list of all stores.
    """
    permission_classes = [AllowAny]
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

# API view to get the menu for a specific store (public)
class MenuListView(generics.ListAPIView):
    """
    Retrieves the menu list for a specific store.
    """
    permission_classes = [AllowAny]
    serializer_class = MenuSerializer

    def get_queryset(self):
        # Filter menu items by the 'store_id' from the URL parameters
        store_id = self.kwargs["store_id"]
        return Menu.objects.filter(store_id=store_id)

# API View for owner to create a new store
class OwnerStoreCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsUserType]
    user_type = 'owner'
    serializer_class = StoreCreateSerializer