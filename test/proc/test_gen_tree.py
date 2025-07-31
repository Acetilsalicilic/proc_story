from proc.npc.GenTree import GenTree
from proc.npc.NPC import NPC

import unittest

class TestGenTree(unittest.TestCase):
    def test_init_tree_gen(self):
        n1 = NPC('1', 'female', 'Eva')
        n2 = NPC('2', 'male', 'Adan')

        gt = GenTree(n1, n2)
        dm = gt.get_dist_mat()
        dm.print_matrix()

if __name__ == '__main__':
    unittest.main()