import logging

from own_logging.simulation.simulationLogger import SimulationLogger


class SimulationRunnerLogger:
    __logger: logging.Logger

    def __init__(self, filename: str, name: str, module_name: str, level = logging.INFO, mode: str = 'a'):
        self.__logger = logging.getLogger(f'{module_name}.{name}_logger')
        self.__logger.setLevel(level)

        formatter = logging.Formatter("RUNNER %(message)s")
        handler = logging.FileHandler(filename, mode)

        self.__logger.addHandler(handler)
    

    def message(self, message: str):
        self.__logger.debug(message)
    

    def get_simulation_logger(self, name: str, number: int, file: str) -> SimulationLogger:
        return SimulationLogger(file, number, name, name, __name__)