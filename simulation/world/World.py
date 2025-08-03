'''
This is the world.
It's a single simulation unit. Contains all the info of the simulation.
'''

from world.organisations import WorldConfig
from world.Cell import Cell


class World:
    __ideologies: list
    __civilizations: list
    __cell_mesh: list[list[Cell]]
    __config: WorldConfig

    def __init__(self, config: WorldConfig):
        self.__config = config

        # start the setup process
        