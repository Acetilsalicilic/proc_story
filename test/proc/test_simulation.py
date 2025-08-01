import unittest

from proc.main_simulation import ProceduralSimulation

class TestSimulation(unittest.TestCase):
    def test_ten_steps(self):
        simulation = ProceduralSimulation(1)
        simulation.simulate(10)
        simulation.report_simulation()