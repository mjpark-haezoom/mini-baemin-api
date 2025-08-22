# stores/models.py

from django.db import models


class Store(models.Model):
    """Model to store information about a store."""
    name = models.CharField(max_length=100, verbose_name="Store name")
    address = models.CharField(max_length=255, verbose_name="Address")
    phone_number = models.CharField(max_length=20, verbose_name="Phone number")

    def __str__(self):
        return self.name

class Menu(models.Model):
    """Model to store menu item information."""
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="menus",
        verbose_name="Store",
    )
    name = models.CharField(max_length=100, verbose_name="Menu name")
    description = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")

    def __str__(self):
        return f"{self.store.name} - {self.name}"