import logging

from simulation.world.terrain.terrain import Terrain
from simulation.world.terrain.terrainPrinting import get_terrain_str_repr


class SimulationLogger:
    __logger: logging.Logger

    def __init__(self, filename: str, sim_no: int, sim_name: str, logger_name: str, module_name: str, level = logging.INFO, mode: str = 'w'):
        self.__logger = logging.getLogger(f'{module_name}.{logger_name}_logger')
        self.__logger.setLevel(level)

        formatter = logging.Formatter(f"SIMULATION ({sim_name}) %(message)s")
        handler = logging.FileHandler(filename, mode)
        handler.setFormatter(formatter)

        self.__logger.addHandler(handler)
    
    def start_progress(self):
        self.__logger.info('Starting simulation')
    
    def end_progress(self):
        self.__logger.info('Progress ended')
    
    def message(self, message: str):
        self.__logger(message)
    
    def start_report(self):
        self.__logger.info('### REPORT ###')

    def end_report(self):
        self.__logger.info('### END REPORT ###')
    
    def report_terrain(self, terrain: Terrain):
        self.__logger.info(f'*** Terrain ***')
        self.__logger.info(f'Size: ({terrain.size_x}, {terrain.size_y})')
        self.__logger.info(f'Seed: {terrain.seed}')
        for line in get_terrain_str_repr(terrain):
            line_buff = ''
            for sym in line:
                line_buff += sym
            self.__logger.info(line_buff)