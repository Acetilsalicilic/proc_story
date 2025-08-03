'''
This is a single cell.

It represents the spatial logic unit of the world.
'''

from enum import Enum


class CellParameters(Enum):
    ELEVATION = 0
    HUMIDITY = 1

class Cell:
    __params: dict[CellParameters:any]

    def __init__(self, params: dict[CellParameters:any]):
        self.__params = params
    
    def get_params(self) -> dict[CellParameters:any]:
        return self.__params