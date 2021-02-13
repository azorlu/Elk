import json
from types import SimpleNamespace

class Inventor:
    """Handles the inventory of requests"""

    def __init__(self, inventory_file):
        self.inventory_file = inventory_file
        self.inventory_data = {}
        with open(inventory_file, "r") as read_file:
            self.inventory_data = json.loads(read_file.read(), object_hook=lambda d: SimpleNamespace(**d))
    
    def get_item(self, item_id):
        for item in self.inventory_data.items:
            if item.id == item_id:
                return item
        return None           
    

