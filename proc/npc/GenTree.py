'''
This GenTree has all the data of the family relationships, that is, inmutable relationships

These are the existing relationships:
- Parent-child
- Sibling
- Partner

The mesh stores data in this way:
mesh = {
    child: {
        parent_1: parent-child,
        parent_2: parent-child
    },
    parent_1: {
        child: parent-child,
        parent_2: partner
    },
    parent_2: {
        child: parent-child,
        parent_1: partner
    }
}

Now, how about incest?
Picture this: Adan and Eva have a son, now, that man has a child with Eva, his
mother. What should it be? Say that the baby is a woman. Now, that woman is the daughter of
the son, but also his sister. Now this: the son has a child WITH his sister.

Now, this is the thing: Adan and Eva are gen 0, cause they're founders.
The son is gen 1, cause is the first child. Now, the sister-daughter must be in the same
gen as the son, cause it's the child of Eva. When brother and sister have a child, that child
is now gen 2. If for example the sister had a child with Adan, then that child would be gen 1 too.

Alright, that makes this soo complicated. Let's do it so there can't be inter-gen breeding.
But then, far cousins couldn't have children?
'''

from enum import Enum
from .NPC import NPC, NPCError, calculate_mutual_compat, create_npc

class RelationType(Enum):
    PARENT_CHILD = 0
    SIBLING = 1

class GenTree:
    __mesh: dict[NPC:dict[NPC:str]]


    def __init__(self, adan: NPC, eva: NPC):
        self.__mesh = {}
        self.__people_counter = 0

        self.__mesh[adan] = {}
        self.__mesh[eva] = {}

        # set the generation for these folks - it's 0, cause they're founders
        adan.set_gen(0)
        eva.set_gen(0)

        # add two to the counter
        self.__people_counter += 2


    def get_relations(self, npc: NPC) -> dict[NPC:str]:
        return self.__mesh.get(npc, {})
    

    # Adding new people to these trees only happens when one is born, so
    # two parents must be involved to start
    def add_npc(self, npc: NPC, parent1: NPC, parent2: NPC) -> None: # Breed!
        # New NPC cannot be in mesh
        if npc in self.__mesh:
            raise GenTreeIntegrityError("New NPC already in mesh")
        
        # Cannot ue the same NPC for breeding
        if parent1 == parent2:
            raise GenTreeIntegrityError("Parents cannot be the same NPC")
        
        # Both parents must be already in mesh
        if parent1 not in self.__mesh or parent2 not in self.__mesh:
            raise GenTreeIntegrityError("Parents aren't on mesh")
        
        # parents must be on the same generation - sorry!
        if parent1.get_gen() != parent2.get_gen():
            raise GenTreeIntegrityError("Parents must be of the same generation")

        # add the new npc
        self.__mesh[npc] = {}

        # set the npc generation
        npc.set_gen(parent1.get_gen() + 1)

        # add the parent relationship
        self.__mesh[npc][parent1] = RelationType.PARENT_CHILD
        self.__mesh[npc][parent2] = RelationType.PARENT_CHILD

        # add the relationships to the parents too
        self.__mesh[parent1][npc] = RelationType.PARENT_CHILD
        self.__mesh[parent2][npc] = RelationType.PARENT_CHILD

        # determine brothers too
        # relation with parents
        possible_siblings = set()
        for person, relation in self.__mesh[parent1].items():
            if relation == RelationType.PARENT_CHILD:
                possible_siblings.add(person)
        
        for person, relation in self.__mesh[parent2].items():
            if relation == RelationType.PARENT_CHILD:
                possible_siblings.add(person)
        
        # same gen people
        same_gen = set()
        for person in possible_siblings:
            if person.get_gen() == npc.get_gen() and person != npc:
                same_gen.add(person)
        
        # set the relationships
        for person in same_gen:
            self.__mesh[person][npc] = RelationType.SIBLING
            self.__mesh[npc][person] = RelationType.SIBLING


    def print_mesh(self):
        visited = []
        print(f'Persons in mesh: {len(self.__mesh)}')
        for person, relations in self.__mesh.items():
            print(f'Person: {person} - relations: {len(relations)}')
            if person in visited:
                continue
            visited.append(person)

            for relation, type in relations.items():
                print(f'{person} <-> {relation}: {type.name}')
    

    def calc_best_attraction(self, npc: NPC) -> NPC:
        # We must visit all the npcs of the same generation, and then see which has the
        # most mutual attraction
        if npc not in self.__mesh:
            raise GenTreeIntegrityError("NPC must be in mesh")
        
        same_gen = [other for other in self.get_npcs() if other.get_gen() == npc.get_gen() and other != npc]
        print(same_gen)

        # determine who has the best attraction
        best_attraction = float('-inf')
        best_partner = None

        for other in same_gen:
            attraction = calculate_mutual_compat(npc, other)
            if attraction > best_attraction:
                best_attraction = attraction
                best_partner = other
        
        return best_partner

    def get_npcs(self) -> tuple[NPC]:
        return tuple(self.__mesh.keys())

    def get_npc_count(self) -> int:
        return len(self.__mesh)
        


class GenTreeIntegrityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def create_tree() -> GenTree:
    adan = create_npc('Adan')
    eva = create_npc('Eva')

    return GenTree(adan, eva)