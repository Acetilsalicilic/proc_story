from enum import Enum
import random
import uuid


class TraitNames(Enum):
    FUNNY = 0
    SERIOUS = 1
    IRRITABLE = 2
    DEPRESSIVE = 3

POSITIVE_TRAITS = [
    TraitNames.FUNNY,
    TraitNames.SERIOUS
]

NEGATIVE_TRAITS = [
    TraitNames.IRRITABLE,
    TraitNames.DEPRESSIVE
]

MAX_TRAIT_VALUE = 5

class NPC:
    __id: uuid.UUID
    __gen: int
    __name: str
    __own_traits: dict[TraitNames:int]
    __wishes_traits: dict[TraitNames:int]

    def __init__(self, name:str = ''):
        self.__id = uuid.uuid1()
        self.__gen = 0
        self.__name = name

        self.__own_traits = {}
        self.__wishes_traits = {}
    
    def __eq__(self, value):
        if not isinstance(value, NPC):
            return False
        
        return self.__id == value.__id
    
    def __hash__(self):
        return self.__id.int
    
    def __repr__(self):
        return f'NPC({self.__name if self.__name != '' else 'nobody'}, g {self.__gen})'
    
    def get_gen(self):
        return self.__gen
    
    def set_gen(self, gen: int):
        self.__gen = gen
    
    def get_id(self) -> int:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_own_traits(self) -> dict[TraitNames:int]:
        return self.__own_traits

    def update_own_trait(self, trait: TraitNames, value: int) -> None:
        if value < 0:
            raise Exception('Trait value cannot be negative')
        self.__own_traits[trait] = value
    
    def update_wished_trait(self, trait: TraitNames, value: int) -> None:
        if value < 0:
            raise Exception('Trait value cannot be negative')
        self.__wishes_traits[trait] = value
    
    def calc_attraction(self, other_traits: dict[TraitNames:int]) -> float:
        # good traits
        good_wishes = {trait:weight for trait, weight in self.__wishes_traits.items() if trait in POSITIVE_TRAITS}
        sum_compat_good = 0
        sum_weights_good = 0

        if len(good_wishes) == 0:
            raise Exception(f"At least one good wish is required for {self}")

        for trait, weight in good_wishes.items():
            print(f'Good trait: {trait.name}')
            sum_weights_good += weight

            difference = abs(weight - other_traits.get(trait, 0))

            compat = weight * (1 - (difference / MAX_TRAIT_VALUE))
            sum_compat_good += compat
            print(f'weight: {sum_weights_good}\ncompat: {sum_compat_good}')
        
        total_good = sum_compat_good / sum_weights_good

        # bad
        bad_wishes = {trait:weight for trait, weight in self.__wishes_traits.items() if trait in NEGATIVE_TRAITS}
        sum_compat_bad = 0
        sum_weights_bad = 0

        if len(bad_wishes) == 0:
            raise Exception("At least one bad wish is required")

        for trait, weight in bad_wishes.items():
            print(f'Bad trait: {trait.name}')
            sum_weights_bad += weight

            difference = abs(weight - other_traits.get(trait, 0))

            compat = weight * (1 - (difference / MAX_TRAIT_VALUE))
            sum_compat_bad += compat
            print(f'weight: {sum_weights_bad}\ncompat: {sum_compat_bad}')
        
        total_bad = sum_compat_bad / sum_weights_bad

        return total_good - total_bad


def calculate_mutual_compat(n1: NPC, n2: NPC) -> float:
    first = n1.calc_attraction(n2.get_own_traits())
    second = n2.calc_attraction(n1.get_own_traits())
    return (first + second) / 2


def create_npc(name: str = '', parent1: NPC = None, parent2: NPC = None) -> NPC:
    if not name:
        new_name = parent1.get_name().split(' ')[0] + ' ' + parent2.get_name().split(' ')[0]
        npc = NPC(new_name)
    else:
        npc = NPC(name)

    # define the traits
    for trait in TraitNames:
        will_have = random.random() > 0.5

        if will_have:
            npc.update_own_trait(trait, random.randint(1, MAX_TRAIT_VALUE))
    
    # define the wishes
    for trait in TraitNames:
        will_wish = random.random() > 0.5

        if will_wish:
            npc.update_wished_trait(trait, random.randint(1, MAX_TRAIT_VALUE))
    
    return npc


class NPCError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
'''
        Desirability
        < 0 - bad
        > 0 - good

        Desirability is calculated on the compatibility of other's traits and own's wished traits.
        So, if someone wishes for a person that's funny with a weight of 3, and the other person is
        funny in 1, 
        '''