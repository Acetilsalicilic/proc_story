from enum import Enum
import logging
from sys import exception, stderr, stdout

from proc.SimulationError import SimulationError
from proc.npc.GenTree import GenTree

class LoggingError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class ProgressLogger:
    __logger = logging.Logger
    __started: bool
    __stdout_logger: logging.Logger

    def __init__(self, filename: str, module_name: str, name: str = 'ProgressLogger', mode: str = 'w'):
        self.__started = False
        self.__logger = logging.getLogger(f'{module_name}.{name}')
        self.__logger.setLevel(logging.INFO)

        # set the format fot this thing
        formatter = logging.Formatter('Progress: %(message)s')
        handler = logging.FileHandler(filename=filename, mode=mode, encoding='utf-8')

        handler.setFormatter(formatter)

        self.__logger.addHandler(handler)

        # set the formatting fo the std logger
        handler = logging.StreamHandler(stdout)
        handler.setFormatter(formatter)

        self.__logger.addHandler(handler)
    
    def start_report(self) -> None:
        if (self.__started):
            raise LoggingError('This progress logger has already been initiated')
        self.__started = True

        self.__logger.info('--- Simulation progress ---')
    
    def end_report(self) -> None:
        self.__logger.info('--- Simulation end ---')
    
    def print_step(self, step: int, total: int) -> None:
        self.__logger.info(f'Step {step} of {total}')


class SimReportLogger:
    __logger: logging.Logger

    def __init__(self, filename: str, module_name: str, name: str = 'ReportLogger', mode: str = 'a', level: any = logging.DEBUG):
        self.__logger = logging.getLogger(f'{module_name}.{name}')
        self.__logger.setLevel(level)

        formatter = logging.Formatter('Report: %(message)s')
        handler = logging.FileHandler(filename=filename, mode=mode, encoding='utf-8')
        handler.setFormatter(formatter)

        self.__logger.addHandler(handler)
    

    def start_report(self):
        self.__logger.info('### REPORT ###')
    

    def end_report(self):
        self.__logger.info('### END REPORT ###')
    

    def basic_stats(self, trees: list[GenTree]):

        self.__logger.info(f'{len(trees)} trees created')
        npc_count = 0
        for tree in trees:
            npc_count += tree.get_npc_count()

        self.__logger.info(f'{npc_count} NPCs created')
    

    def print_trees(self, trees: list[GenTree]):
        self.__logger.info('*** TREES ***')
        tree_count = len(trees)
        for index, tree in enumerate(trees):
            self.__logger.info(f'Tree {index + 1} of {tree_count}:')
            lines = tree.get_str_mesh()

            for line in lines:
                self.__logger.info(line)
        self.__logger.info('*** END TREES ***')
    

    def gen_info(self, gen_info: dict):
        self.__logger.info('*** GENERATION INFO ***')
        for line, contents in gen_info.items():
            self.__logger.info(f'{line + 1}:')
            for field, value in contents.items():
                self.__logger.info(f'    {field.name} - {value}')
        self.__logger.info('*** END GEN INFO ***')
    

    def detailed_npc_info(self, trees: list[GenTree]):
        self.__logger.debug('*** NPC INFO ***')
        tree_count = len(trees)
        for index, tree in enumerate(trees):
            self.__logger.debug(f'# Tree {index + 1} of {tree_count}')
            curr_tree_npc_count = tree.get_npc_count()
            for npc_no, npc in enumerate(tree.get_npcs()):
                self.__logger.debug(f'# NPC {npc_no + 1} of {curr_tree_npc_count}')
                self.__logger.debug(f'    Name: {npc.get_name()}')
                self.__logger.debug(f'    Gen: {npc.get_gen()}')
                self.__logger.debug(f'    Traits: {npc.get_own_traits()}')
                self.__logger.debug(f'    Wished traits: {npc.get_woshed_traits()}')

                # relationships
                curr_npc_relationships = tree.get_relations(npc)
                for other, rel_type in curr_npc_relationships.items():
                    self.__logger.debug(f'    {other} <> {rel_type.name}')
        self.__logger.debug('*** END NPC INFO ***')

class SimAbortLogger:
    __logger: logging.Logger
    __exception: Exception

    def __init__(self, filename: str, module_name: str, name: str = 'AbortLogger', mode: str = 'a'):
        self.__logger = logging.getLogger(f'{module_name}.{name}')
        self.__logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('ABORT - %(levelname)s: %(message)s')
        file_handler = logging.FileHandler(filename, mode, 'utf-8')
        stderr_handler = logging.StreamHandler(stderr)

        file_handler.setFormatter(formatter)
        stderr_handler.setFormatter(formatter)

        self.__logger.addHandler(file_handler)
        self.__logger.addHandler(stderr_handler)
    

    def abort_simulation(self, exception: SimulationError):
        self.__logger.error('+++ SIMULATION ABORTED +++')
        self.__logger.error(f'Cause: {type(exception)}, message: {exception.get_message()}')
        self.__logger.exception(exception)

        self.__exception = exception
    

    def end_abort(self):
        self.__logger.error('+++ END ABORT +++')

        raise self.__exception
    

    def print_trees(self, trees: list[GenTree]):
        self.__logger.error('*** TREES ***')
        tree_count = len(trees)
        for index, tree in enumerate(trees):
            self.__logger.error(f'Tree {index + 1} of {tree_count}')
            lines = tree.get_str_mesh()
            for line in lines:
                self.__logger.error(line)
        self.__logger.error('*** END TREES ***')