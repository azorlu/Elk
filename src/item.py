from types import SimpleNamespace
from .query import Query

class Item:
    """Inventory item"""

    def __init__(self, inventory_item):
        self.id = inventory_item.id
        self.url = inventory_item.url
        self.query = Query(inventory_item.query)