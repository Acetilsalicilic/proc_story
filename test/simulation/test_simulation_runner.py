import unittest

from simulation.config.mainConfigLoader import MainConfigurationLoader
from simulation.simulationRunner import SimulationRunner

class TestSimRuner(unittest.TestCase):
    def test_simulation_runer(self):
        # load the configs
        config_loader = MainConfigurationLoader('test_config.json')

        configs = config_loader.get_sim_config()

        runner = SimulationRunner(configs)

        # run it!
        runner.create_simulations()
        runner.run_simulations()