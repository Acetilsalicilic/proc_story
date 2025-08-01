'''
This script is responsible for the simulation proces BEFORE gameplay

For now, this only simulates family tree creation
'''

from enum import Enum
from proc.npc.GenTree import GenTree
from proc.npc.GenTree import create_tree
from proc.npc.NPC import create_npc


class SimulationError(Exception):
    __message: str
    def __init__(self, message: str):
        self.__message = message
        super().__init__(message)
    
    def get_message(self) -> str:
        return self.__message
    
class GenerationInfoField(Enum):
    NPC_COUNT = 0


class ProceduralSimulation:
    __trees: list[GenTree]
    __tree_goal: int
    __simulated: bool
    __generation_info: dict

    # TODO: Implement file-logging system - Maybe a third party logger??

    def __init__(self, tree_no: int):
        self.__tree_goal = tree_no
        self.__simulated = False
        self.__trees = []
        self.__generation_info = {}

    def simulate(self, steps: int):
        # simulation can run only once
        if self.__simulated:
            raise SimulationError("This simulation has already been run")
        self.__simulated = True

        print('---SIMULATION STARTS---')
        # get the trees
        for i in range(self.__tree_goal):
            self.__trees.append(create_tree())

        # Procceed with the simulation
        for step in range(steps):
            print(f'Step: {step + 1} of {steps}')
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
        print('---SIMULATION FINISHED---')

    def cancel_simulation(self, exception: SimulationError):
        print('+++ SIMULATION ABORTED +++')

        print(f'Cause: {type(exception)}, message: {exception.get_message()}')

        print('***TREES***')
        for index, tree in enumerate(self.__trees):
            print(f'Tree {index}:')
            tree.print_mesh()
        print('***END TREES***')
        print('*** END ABORT ***')

        raise exception
    
    def report_simulation(self) -> None:
        print('### REPORT ###')
        print(f'{len(self.__trees)} created')
        npc_count = 0
        for tree in self.__trees:
            npc_count += tree.get_npc_count()
        print(f'{npc_count} NPCs created')

        # print trees
        print('***TREES***')
        for index, tree in enumerate(self.__trees):
            print(f'Tree {index}:')
            tree.print_mesh()
        print('***END TREES***')

        # detailed generation info
        print('*** GENERATION INFO ***')
        for line, contents in self.__generation_info.items():
            print(f'{line + 1}:')
            for field, value in contents.items():
                print(f'    {field.name} - {value}')
        print('*** END GENERATION INFO ***')
        print('### END REPORT ###')


