from types import SimpleNamespace
from .query_type import QueryType

class Query:
    """Inventory item query"""

    def __init__(self, inventory_item_query):
        self.query_type = QueryType.NONE

        if hasattr(inventory_item_query, 'name'):
            self.name = inventory_item_query.name
            self.query_type |= QueryType.NAME
        else:
            self.name = None
        if hasattr(inventory_item_query, 'limit'):
            self.limit = inventory_item_query.limit
            self.is_limit_set = True
        else:
            self.limit = None
            self.is_limit_set = False
        if hasattr(inventory_item_query, 'recursive'):
            self.recursive = inventory_item_query.recursive
            self.is_recursive_set = True
        else:
            self.recursive = None
            self.is_recursive_set = False
        if hasattr(inventory_item_query, 'string'):
            self.string = inventory_item_query.string
            self.query_type |= QueryType.STRING
        else:
            self.string = None
        if hasattr(inventory_item_query, 'kwargs'):
            self.kwargs = inventory_item_query.kwargs
        else:
            self.kwargs = None
        if hasattr(inventory_item_query, 'attrs'):
            # casting to dict is required
            self.attrs = vars(inventory_item_query.attrs)
        else:
            self.attrs = None
        