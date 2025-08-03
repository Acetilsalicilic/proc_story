from simulation.config.simulationConfig import SimulationConfig
from simulation.world.terrain.terrainPrinting import get_terrain_str_repr, print_to_stdout
from simulation.world.terrain.terrain import Terrain
from simulation.world.terrain.terrainGenerator import TerrainGenerator


class Simulation:
    __config: SimulationConfig
    __terrain: Terrain


    def __init__(self, config: SimulationConfig):
        self.__config = config

    def get_name(self) -> str:
        return self.__config.name

    def simulate(self) -> None:
        self.__generate_terrain()
        self.__report()


    def __generate_terrain(self):
        terrain_config = self.__config.terrain_conf

        terr_generator = TerrainGenerator(terrain_config)
        terr_generator.generate_pnoise()
        self.__terrain = terr_generator.create_terrain()
    

    def __report(self):
        print_to_stdout(get_terrain_str_repr(self.__terrain))

