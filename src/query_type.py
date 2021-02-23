from enum import Flag, auto

class QueryType(Flag):
    """Inventory item query type"""
    NONE = 0
    NAME = auto()
    STRING = auto()
    NAME_STRING = NAME | STRING