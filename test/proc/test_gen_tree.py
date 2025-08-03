import unittest

from proc.npc.GenTree import GenTree
from proc.npc.GenTree import GenTreeIntegrityError
from proc.npc.NPC import NPC

class TestGenTree(unittest.TestCase):
    def test_tree_creation(self):
        print('---CREATION---')
        adan = NPC()
        eva = NPC()
        gen_tree = GenTree(adan, eva)

        gen_tree.print_mesh()
    
    def test_first_child(self):
        print('---FIRST CHILD---')
        adan = NPC('Adan')
        eva = NPC('Eva')
        child = NPC('Cain')

        gen_tree = GenTree(adan, eva)

        gen_tree.add_npc(child, adan, eva)

        gen_tree.print_mesh()
    
    def test_second_child(self):
        print('---SECOND CHILD---')
        adan = NPC('Adan')
        eva = NPC('Eva')
        cain = NPC('Cain')
        abel = NPC('Abel')

        gen_tree = GenTree(adan, eva)

        gen_tree.add_npc(cain, adan, eva)
        gen_tree.add_npc(abel, adan, eva)

        gen_tree.print_mesh()
    
    def test_no_intergeneration(self):
        print('---INCEST---')
        adan = NPC('Adan')
        eva = NPC('Eva')
        cain = NPC('Cain')
        child = NPC('Bad one')

        gen_tree = GenTree(adan, eva)

        gen_tree.add_npc(cain, adan, eva)
        self.assertRaises(GenTreeIntegrityError, gen_tree.add_npc, child, cain, eva)

        gen_tree.print_mesh()
    
    def test_non_existent(self):
        print('---NON EXISTENT---')
        first = NPC('First')
        second = NPC('SECOND')
        child = NPC('child')
        nobody = NPC()

        gen_tree = GenTree(first, second)
        self.assertRaises(GenTreeIntegrityError, gen_tree.add_npc, child, first, nobody)
    
    def test_insert_again(self):
        adan = NPC('Adan')
        eva = NPC('Eva')
        child = NPC('Cain')

        gen_tree = GenTree(adan, eva)

        gen_tree.add_npc(child, adan, eva)
        self.assertRaises(GenTreeIntegrityError, gen_tree.add_npc, adan, child, eva)
