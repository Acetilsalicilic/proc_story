from own_logging.simulation.simulationLogger import SimulationLogger
from simulation.config.simulationConfig import SimulationConfig
from simulation.world.terrain.terrainPrinting import get_terrain_str_repr, print_to_stdout
from simulation.world.terrain.terrain import Terrain
from simulation.world.terrain.terrainGenerator import TerrainGenerator


class Simulation:
    __config: SimulationConfig
    __terrain: Terrain
    __logger: SimulationLogger


    def __init__(self, config: SimulationConfig, logger: SimulationLogger):
        self.__config = config
        self.__logger = logger

    def get_name(self) -> str:
        return self.__config.name

    def simulate(self) -> None:
        self.__logger.start_progress()
        self.__generate_terrain()
        self.__report()
        self.__logger.end_progress()


    def __generate_terrain(self):
        terrain_config = self.__config.terrain_conf

        terr_generator = TerrainGenerator(terrain_config)
        terr_generator.generate_pnoise()
        self.__terrain = terr_generator.create_terrain()
    

    def __report(self):
        self.__logger.start_report()
        self.__logger.report_terrain(self.__terrain)
        self.__logger.end_report()

