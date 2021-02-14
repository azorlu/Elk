from types import SimpleNamespace

class Query:
    """Inventory item query"""

    def __init__(self, inventory_item_query):
        self.name = inventory_item_query.name
        self.limit = inventory_item_query.limit
        self.recursive = inventory_item_query.recursive
        self.string = inventory_item_query.string
        self.kwargs = inventory_item_query.kwargs
        # casting to dict is required
        self.attrs = vars(inventory_item_query.attrs)