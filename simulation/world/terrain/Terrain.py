'''
This terrain instance holds info of the terrain
'''

from simulation.world.Cell import Cell


class Terrain:
    size_x: int
    size_y: int
    cells: list[list[Cell]]
    noise: list[list[float]]
    
    def __init__(self, size: tuple[int], cells, noise):
        self.size_x, self.size_y = size
        self.cells = cells
        self.noise = noise
