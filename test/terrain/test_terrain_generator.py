import unittest

from simulation.world.terrain.terrainGenerator import TerrainConfig, TerrainGenerator
from simulation.world.terrain.terrainPrinting import get_terrain_str_repr, print_to_stdout

class TestTerrainGen(unittest.TestCase):
    def test_generate_terrain(self):
        terr_config = TerrainConfig(20, 20, 4, 10.0, 0.2)
        terr_gen = TerrainGenerator(terr_config)

        terr_gen.generate_pnoise()
        terrain = terr_gen.create_terrain()

        print_to_stdout(get_terrain_str_repr(terrain))
