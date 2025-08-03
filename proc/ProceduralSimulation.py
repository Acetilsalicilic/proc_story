'''
This script is responsible for the simulation proces BEFORE gameplay

For now, this only simulates family tree creation
'''

from enum import Enum
from sim_logging.ProcLogger import ProgressLogger, SimAbortLogger
from sim_logging.ProcLogger import SimReportLogger
from proc.npc.GenTree import GenTree, RelationType
from proc.npc.GenTree import create_tree
from proc.npc.NPC import create_npc
from .SimulationError import SimulationError
    
class GenerationInfoField(Enum):
    NPC_COUNT = 0


class ProceduralSimulation:
    __trees: list[GenTree]
    __tree_goal: int
    __simulated: bool
    __generation_info: dict

    __proc_logger: ProgressLogger
    __report_logger: SimReportLogger
    __abort_logger: SimAbortLogger

    # TODO: Implement file-logging system - Maybe a third party logger??

    def __init__(self, tree_no: int, proc_logger: ProgressLogger, report_logger: SimReportLogger, abort_logger: SimAbortLogger):
        self.__tree_goal = tree_no
        self.__simulated = False
        self.__trees = []
        self.__generation_info = {}

        self.__proc_logger = proc_logger
        self.__report_logger = report_logger
        self.__abort_logger = abort_logger

    def simulate(self, steps: int):
        # simulation can run only once
        if self.__simulated:
            raise SimulationError("This simulation has already been run")
        self.__simulated = True

        self.__proc_logger.start_report()
        # get the trees
        for i in range(self.__tree_goal):
            self.__trees.append(create_tree())

        # Procceed with the simulation
        for step in range(steps):
            self.__proc_logger.print_step(step + 1, steps)
            self.__generation_info[step] = {}

            # We must traverse each tree
            npc_count = 0
            for tree in self.__trees:
                # We must decide who will breed with who
                visited = []
                for npc in tree.get_npcs():
                    if npc in visited:
                        continue

                    partner = None
                    try:
                        partner = tree.calc_best_attraction(npc)
                    except:
                        self.cancel_simulation(SimulationError(f'Failed to determine a partner for {npc}'))

                    try:
                        visited.append(npc)
                        visited.append(partner)

                        # create the child
                        child = create_npc(parent1=npc, parent2=npc)

                        # add child to the tree
                        tree.add_npc(child, npc, partner)
                    except:
                        self.cancel_simulation(SimulationError(f'{npc} tried to mate with {partner}'))
                    
                npc_count += tree.get_npc_count()
            
            self.__generation_info[step][GenerationInfoField.NPC_COUNT] = npc_count
        self.__proc_logger.end_report()

    def cancel_simulation(self, exception: SimulationError):
        self.__abort_logger.abort_simulation(exception)
        self.__abort_logger.print_trees(self.__trees)
        self.__abort_logger.end_abort()
    
    
    def report_simulation(self) -> None:
        self.__report_logger.start_report()
        self.__report_logger.basic_stats(self.__trees)

        # print trees
        self.__report_logger.print_trees(self.__trees)

        # detailed generation info
        self.__report_logger.gen_info(self.__generation_info)

        # detailed npc info
        self.__report_logger.detailed_npc_info(self.__trees)

        # end
        self.__report_logger.end_report()