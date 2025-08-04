'''
This class is meant to load the configuration
'''


import json
from simulation.config import simulationConfig
from simulation.config.terrainConfig import TerrainConfig
from simulation.world.terrain.terrain import Terrain
from own_logging.simulation.simulationRunnerLogger import SimulationRunnerLogger


class MainConfigurationLoader:
    __filename: str
    __format: str

    __sim_data: any

    __logger: SimulationRunnerLogger

    def __init__(self, filename: str, logger: SimulationRunnerLogger, format: str = 'json'):
        self.__logger = logger

        self.__filename = filename
        self.__format = format

        self.__load_json()

    def __load_json(self):
        # exctract the config for each simulation
        self.__logger.message(f'Loading json from {self.__filename}...')
        with open(self.__filename) as file:
            data = json.load(file)

            self.__sim_data = data['simulations']
        self.__logger.message(f'Loaded:')
        self.__logger.message(self.__sim_data)

    
    def get_sim_config(self) -> list[simulationConfig.SimulationConfig]:
        configs = list()
        for sim_data in self.__sim_data:
            terrain_conf = sim_data['terrain']
            sim_name = sim_data['name']
            log_file = sim_data['log_file']

            terrain_conf_obj = TerrainConfig(
                terrain_conf['size_x'],
                terrain_conf['size_y'],
                terrain_conf['seed'],
                terrain_conf['frequency'],
                terrain_conf['sea_level']
            )
            configs.append(simulationConfig.SimulationConfig(terrain_conf_obj, sim_name, log_file))
        self.__logger.message(f'Returning {len(configs)} from json')
        return configs
            
