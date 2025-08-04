'''
This logger takes care of the simulation part
'''

import logging
from sys import stdout


class ConfigLogger:
    __logger: logging.Logger

    def __init__(self, filename: str, loader_name: str, module_name: str, to_stdout: bool = True, mode: str = 'w'):
        self.__logger = logging.getLogger(f'{module_name}.{loader_name}')
        self.__logger.setLevel(logging.DEBUG)

        # formatter
        formatter = logging.Formatter(f"CONFIG [{loader_name}] %(message)s")

        # handler
        file_handler = logging.FileHandler(filename, mode)
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)
        
        if to_stdout:
            stream_handler = logging.StreamHandler(stdout)
            self.__logger.addHandler(stream_handler)
    

    def message(self, message: str):
        self.__logger.debug(message)