'''
This class holds the configuration for a world in a neat and extensible way
'''

from enum import Enum


class WorldConfigFields(Enum):
    CELL_WIDTH = 0
    CELL_HEIGHT = 1


class WorldConfig:
    __value_dict: dict[WorldConfigFields:any]
    __exp_id: str

    def __init__(self, exp_id: str, values: dict):
        self.__exp_id = exp_id
        self.__value_dict = values



    def get(self, value: WorldConfigFields, default: any = None) -> any:
        if value not in WorldConfigFields:
            return default
        
        return self.__value_dict.get(value, default)
