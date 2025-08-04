'''
This terrain generator creates a grid of n x m cells with the desired seed,
being in charge of determining all the terrain and climate characteristics of this thing
'''

import noise

from simulation.world import cell
from simulation.world.terrain.terrain import Terrain
from simulation.config.terrainConfig import TerrainConfig


class TerrainGenerator:
    __seed: int
    __size_x: int
    __size_y : int
    __frequency: float

    # __noise_grid[x][y]
    __noise_grid: list[list[float]]

    __populated: bool
    __config: TerrainConfig

    def __init__(self, config: TerrainConfig):
        self.__config = config

        self.__seed = config.seed
        self.__populated = False

        self.__size_x = config.size_x
        self.__size_y = config.size_y

        self.__frequency = config.frequency


        # create the grid
        self.__noise_grid = list()
        for i in range(self.__size_y):
            self.__noise_grid.append(list())
    

    def generate_pnoise(self):
        if self.__populated:
            raise TerrainError('Cannot populate the terrain generator again')
        self.__populated = True

        # populate the grid
        for x_index, row in enumerate(self.__noise_grid):
            for y_index in range(self.__size_y):
                row.append(noise.pnoise2(x_index / self.__frequency, y_index / self.__frequency, base=self.__seed))
    

    def create_terrain(self) -> Terrain:
        # initialize the cell grid
        cell_grid = list()

        for row in range(self.__size_x):
            cell_grid.append(list())
            for y_index in range(self.__size_y):
                cell_grid[-1].append(0.0)
        
        # populate the cell
        for x_pos in range(self.__size_x):
            for y_pos in range(self.__size_y):
                elevation = self.__noise_grid[x_pos][y_pos]
                humidity = 1 if elevation < self.__config.sea_level else 0

                cell_grid[x_pos][y_pos] = cell.Cell(elevation, humidity)
        
        return Terrain(size_x=self.__size_x, size_y=self.__size_y, cells=cell_grid, noise=self.__noise_grid, seed=self.__seed)


class TerrainError(Exception):
    def __init__(self, *args):
        super().__init__(*args)