'''
A gen tree is a genealogical tree. It's basically a graph with level tracking,
so determining relationships is sanely possible.

This gen tree must start with two starting NPCs

This graph must store the following:
- An NPC reference
- A reference to all of the NPC's it has a relationship with
- The distance to that relationship

So it would look something like this:
graph: {
    'NPC 1': {
        'NPC 2': 1,
        'NPC 3': 2
    },
    'NPC 2': {
        'NPC 1': 1,
        'NPC 3': 1,
    },
    'NPC 3': {
        'NPC 1': 2,
        'NPC 2': 1
    }
}
'''

from .NPC import NPC

RELATION_TYPES = (
    'parent',
    'child',
    'sibling'
)


class DistanceMatrix:
    __matrix: dict[NPC:dict[NPC:int]]

    def __init__(self):
        self.__matrix = {}

    def get_distance(self, npc1: NPC, npc2: NPC) -> int:
        dist1 = self.__matrix.get(npc1, {}).get(npc2)
        dist2 = self.__matrix.get(npc2, {}).get(npc1)

        if dist1 != dist2:
            raise DistMatrixInconsistencyError("Inconsistency in distances")
        
        return dist1
    
    
    def insert_distance(self, npc1: NPC, npc2: NPC, dist: int) -> None:
        # initialize sub-objects if they don't exist
        if npc1 not in self.__matrix:
            self.__matrix[npc1] = {}
        if npc2 not in self.__matrix:
            self.__matrix[npc2] = {}
        
        # set the distances on the sub-objects
        self.__matrix[npc1][npc2] = dist
        self.__matrix[npc2][npc1] = dist
    
    def print_matrix(self):
        for npc1, relations in self.__matrix.items():
            for npc2, dist in relations.items():
                print(f'{npc1.get_name()} <-> {npc2.get_name()}: {dist}')


class GenTree:
    __distMat: DistanceMatrix
    __generation_dict: dict[NPC:int]

    def __init__(self, npc1: NPC, npc2: NPC):
        self.__distMat = DistanceMatrix()

        # add the first two relationships from Adan and Eva
        self.__distMat.insert_distance(npc1, npc2, 1)
    

    def get_generation(self, npc: NPC) -> int:
        return self.__generation_dict[npc]
    
    def get_dist_mat(self) -> DistanceMatrix:
        return self.__distMat
    
    def get_relationship(self, n1: NPC, n2: NPC) -> dict[NPC:str]:
        # we need their generation and their distance
        gen1 = self.get_generation(n1)
        gen2 = self.get_generation(n2)
        dist = self.__distMat.get_distance(n1, n2)

        '''
        Rules for relationships:
        
        '''


class DistMatrixInconsistencyError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

def simulate_generation(tree: GenTree) -> None:
    pass
