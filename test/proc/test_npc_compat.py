import unittest

from proc.npc.NPC import NPC
from proc.npc.NPC import TraitNames

class TestNPCCompat(unittest.TestCase):
    def test_positive_compat(self):
        print('---POSITIVE COMPAT---')
        n1 = NPC('Adam')
        n2 = NPC('Eve')

        n1.update_own_trait(TraitNames.FUNNY, 4)
        n2.update_wished_trait(TraitNames.FUNNY, 3)

        n1.update_own_trait(TraitNames.IRRITABLE, 2)
        n2.update_wished_trait(TraitNames.IRRITABLE, 4)

        self.assertGreater(n2.calc_attraction(n1.get_own_traits()), 0)
    
    def test_negative_compat(self):
        print('---NEGATIVE COMPAT---')
        n1 = NPC('Adam')
        n2 = NPC('Eve')

        n1.update_own_trait(TraitNames.FUNNY, 3)
        n2.update_wished_trait(TraitNames.FUNNY, 1)

        n1.update_own_trait(TraitNames.IRRITABLE, 2)
        n2.update_wished_trait(TraitNames.IRRITABLE, 3)


        self.assertLess(n2.calc_attraction(n1.get_own_traits()), 0)