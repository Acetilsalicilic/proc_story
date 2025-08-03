import unittest

from simulation.world.terrain.TerrainGenerator import TerrainGenerator, TerrainRules
from simulation.world.terrain.TerrainPrinter import get_terrain_str_repr, print_to_stdout

class TestTerrainGen(unittest.TestCase):
    def test_generate_terrain(self):
        terr_gen = TerrainGenerator({
            TerrainRules.SEED : 5,
            TerrainRules.SIZE_X : 10,
            TerrainRules.SIZE_Y : 10,
            TerrainRules.SEA_LEVEL : 0.5,
            TerrainRules.FREQUENCY : 10.0
        })

        terr_gen.generate_pnoise()
        terrain = terr_gen.create_terrain()

        print_to_stdout(get_terrain_str_repr(terrain))
