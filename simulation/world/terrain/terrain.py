'''
This terrain instance holds info of the terrain
'''

from dataclasses import dataclass
from simulation.world.cell import Cell

@dataclass
class Terrain:
    size_x: int
    size_y: int
    cells: list[list[Cell]]
    noise: list[list[float]]